# ext/compiler.py
# Copyright (C) 2005-2023 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php
# mypy: ignore-errors

r"""Provides an API for creation of custom ClauseElements and compilers.

Synopsis
========

Usage involves the creation of one or more
:class:`~sqlalchemy.sql.expression.ClauseElement` subclasses and one or
more callables defining its compilation::

    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.sql.expression import ColumnClause

    class MyColumn(ColumnClause):
        inherit_cache = True

    @compiles(MyColumn)
    def compile_mycolumn(element, compiler, **kw):
        return "[%s]" % element.name

Above, ``MyColumn`` extends :class:`~sqlalchemy.sql.expression.ColumnClause`,
the base expression element for named column objects. The ``compiles``
decorator registers itself with the ``MyColumn`` class so that it is invoked
when the object is compiled to a string::

    from sqlalchemy import select

    s = select(MyColumn('x'), MyColumn('y'))
    print(str(s))

Produces::

    SELECT [x], [y]

Dialect-specific compilation rules
==================================

Compilers can also be made dialect-specific. The appropriate compiler will be
invoked for the dialect in use::

    from sqlalchemy.schema import DDLElement

    class AlterColumn(DDLElement):
        inherit_cache = False

        def __init__(self, column, cmd):
            self.column = column
            self.cmd = cmd

    @compiles(AlterColumn)
    def visit_alter_column(element, compiler, **kw):
        return "ALTER COLUMN %s ..." % element.column.name

    @compiles(AlterColumn, 'postgresql')
    def visit_alter_column(element, compiler, **kw):
        return "ALTER TABLE %s ALTER COLUMN %s ..." % (element.table.name,
                                                       element.column.name)

The second ``visit_alter_table`` will be invoked when any ``postgresql``
dialect is used.

.. _compilerext_compiling_subelements:

Compiling sub-elements of a custom expression construct
=======================================================

The ``compiler`` argument is the
:class:`~sqlalchemy.engine.interfaces.Compiled` object in use. This object
can be inspected for any information about the in-progress compilation,
including ``compiler.dialect``, ``compiler.statement`` etc. The
:class:`~sqlalchemy.sql.compiler.SQLCompiler` and
:class:`~sqlalchemy.sql.compiler.DDLCompiler` both include a ``process()``
method which can be used for compilation of embedded attributes::

    from sqlalchemy.sql.expression import Executable, ClauseElement

    class InsertFromSelect(Executable, ClauseElement):
        inherit_cache = False

        def __init__(self, table, select):
            self.table = table
            self.select = select

    @compiles(InsertFromSelect)
    def visit_insert_from_select(element, compiler, **kw):
        return "INSERT INTO %s (%s)" % (
            compiler.process(element.table, asfrom=True, **kw),
            compiler.process(element.select, **kw)
        )

    insert = InsertFromSelect(t1, select(t1).where(t1.c.x>5))
    print(insert)

Produces::

    "INSERT INTO mytable (SELECT mytable.x, mytable.y, mytable.z
                          FROM mytable WHERE mytable.x > :x_1)"

.. note::

    The above ``InsertFromSelect`` construct is only an example, this actual
    functionality is already available using the
    :meth:`_expression.Insert.from_select` method.


Cross Compiling between SQL and DDL compilers
---------------------------------------------

SQL and DDL constructs are each compiled using different base compilers -
``SQLCompiler`` and ``DDLCompiler``.   A common need is to access the
compilation rules of SQL expressions from within a DDL expression. The
``DDLCompiler`` includes an accessor ``sql_compiler`` for this reason, such as
below where we generate a CHECK constraint that embeds a SQL expression::

    @compiles(MyConstraint)
    def compile_my_constraint(constraint, ddlcompiler, **kw):
        kw['literal_binds'] = True
        return "CONSTRAINT %s CHECK (%s)" % (
            constraint.name,
            ddlcompiler.sql_compiler.process(
                constraint.expression, **kw)
        )

Above, we add an additional flag to the process step as called by
:meth:`.SQLCompiler.process`, which is the ``literal_binds`` flag.  This
indicates that any SQL expression which refers to a :class:`.BindParameter`
object or other "literal" object such as those which refer to strings or
integers should be rendered **in-place**, rather than being referred to as
a bound parameter;  when emitting DDL, bound parameters are typically not
supported.


Changing the default compilation of existing constructs
=======================================================

The compiler extension applies just as well to the existing constructs.  When
overriding the compilation of a built in SQL construct, the @compiles
decorator is invoked upon the appropriate class (be sure to use the class,
i.e. ``Insert`` or ``Select``, instead of the creation function such
as ``insert()`` or ``select()``).

Within the new compilation function, to get at the "original" compilation
routine, use the appropriate visit_XXX method - this
because compiler.process() will call upon the overriding routine and cause
an endless loop.   Such as, to add "prefix" to all insert statements::

    from sqlalchemy.sql.expression import Insert

    @compiles(Insert)
    def prefix_inserts(insert, compiler, **kw):
        return compiler.visit_insert(insert.prefix_with("some prefix"), **kw)

The above compiler will prefix all INSERT statements with "some prefix" when
compiled.

.. _type_compilation_extension:

Changing Compilation of Types
=============================

``compiler`` works for types, too, such as below where we implement the
MS-SQL specific 'max' keyword for ``String``/``VARCHAR``::

    @compiles(String, 'mssql')
    @compiles(VARCHAR, 'mssql')
    def compile_varchar(element, compiler, **kw):
        if element.length == 'max':
            return "VARCHAR('max')"
        else:
            return compiler.visit_VARCHAR(element, **kw)

    foo = Table('foo', metadata,
        Column('data', VARCHAR('max'))
    )

Subclassing Guidelines
======================

A big part of using the compiler extension is subclassing SQLAlchemy
expression constructs. To make this easier, the expression and
schema packages feature a set of "bases" intended for common tasks.
A synopsis is as follows:

* :class:`~sqlalchemy.sql.expression.ClauseElement` - This is the root
  expression class. Any SQL expression can be derived from this base, and is
  probably the best choice for longer constructs such as specialized INSERT
  statements.

* :class:`~sqlalchemy.sql.expression.ColumnElement` - The root of all
  "column-like" elements. Anything that you'd place in the "columns" clause of
  a SELECT statement (as well as order by and group by) can derive from this -
  the object will automatically have Python "comparison" behavior.

  :class:`~sqlalchemy.sql.expression.ColumnElement` classes want to have a
  ``type`` member which is expression's return type.  This can be established
  at the instance level in the constructor, or at the class level if its
  generally constant::

      class timestamp(ColumnElement):
          type = TIMESTAMP()
          inherit_cache = True

* :class:`~sqlalchemy.sql.functions.FunctionElement` - This is a hybrid of a
  ``ColumnElement`` and a "from clause" like object, and represents a SQL
  function or stored procedure type of call. Since most databases support
  statements along the line of "SELECT FROM <some function>"
  ``FunctionElement`` adds in the ability to be used in the FROM clause of a
  ``select()`` construct::

      from sqlalchemy.sql.expression import FunctionElement

      class coalesce(FunctionElement):
          name = 'coalesce'
          inherit_cache = True

      @compiles(coalesce)
      def compile(element, compiler, **kw):
          return "coalesce(%s)" % compiler.process(element.clauses, **kw)

      @compiles(coalesce, 'oracle')
      def compile(element, compiler, **kw):
          if len(element.clauses) > 2:
              raise TypeError("coalesce only supports two arguments on Oracle")
          return "nvl(%s)" % compiler.process(element.clauses, **kw)

* :class:`.ExecutableDDLElement` - The root of all DDL expressions,
  like CREATE TABLE, ALTER TABLE, etc. Compilation of
  :class:`.ExecutableDDLElement` subclasses is issued by a
  :class:`.DDLCompiler` instead of a :class:`.SQLCompiler`.
  :class:`.ExecutableDDLElement` can also be used as an event hook in
  conjunction with event hooks like :meth:`.DDLEvents.before_create` and
  :meth:`.DDLEvents.after_create`, allowing the construct to be invoked
  automatically during CREATE TABLE and DROP TABLE sequences.

  .. seealso::

    :ref:`metadata_ddl_toplevel` - contains examples of associating
    :class:`.DDL` objects (which are themselves :class:`.ExecutableDDLElement`
    instances) with :class:`.DDLEvents` event hooks.

* :class:`~sqlalchemy.sql.expression.Executable` - This is a mixin which
  should be used with any expression class that represents a "standalone"
  SQL statement that can be passed directly to an ``execute()`` method.  It
  is already implicit within ``DDLElement`` and ``FunctionElement``.

Most of the above constructs also respond to SQL statement caching.   A
subclassed construct will want to define the caching behavior for the object,
which usually means setting the flag ``inherit_cache`` to the value of
``False`` or ``True``.  See the next section :ref:`compilerext_caching`
for background.


.. _compilerext_caching:

Enabling Caching Support for Custom Constructs
==============================================

SQLAlchemy as of version 1.4 includes a
:ref:`SQL compilation caching facility <sql_caching>` which will allow
equivalent SQL constructs to cache their stringified form, along with other
structural information used to fetch results from the statement.

For reasons discussed at :ref:`caching_caveats`, the implementation of this
caching system takes a conservative approach towards including custom SQL
constructs and/or subclasses within the caching system.   This includes that
any user-defined SQL constructs, including all the examples for this
extension, will not participate in caching by default unless they positively
assert that they are able to do so.  The :attr:`.HasCacheKey.inherit_cache`
attribute when set to ``True`` at the class level of a specific subclass
will indicate that instances of this class may be safely cached, using the
cache key generation scheme of the immediate superclass.  This applies
for example to the "synopsis" example indicated previously::

    class MyColumn(ColumnClause):
        inherit_cache = True

    @compiles(MyColumn)
    def compile_mycolumn(element, compiler, **kw):
        return "[%s]" % element.name

Above, the ``MyColumn`` class does not include any new state that
affects its SQL compilation; the cache key of ``MyColumn`` instances will
make use of that of the ``ColumnClause`` superclass, meaning it will take
into account the class of the object (``MyColumn``), the string name and
datatype of the object::

    >>> MyColumn("some_name", String())._generate_cache_key()
    CacheKey(
        key=('0', <class '__main__.MyColumn'>,
        'name', 'some_name',
        'type', (<class 'sqlalchemy.sql.sqltypes.String'>,
                 ('length', None), ('collation', None))
    ), bindparams=[])

For objects that are likely to be **used liberally as components within many
larger statements**, such as :class:`_schema.Column` subclasses and custom SQL
datatypes, it's important that **caching be enabled as much as possible**, as
this may otherwise negatively affect performance.

An example of an object that **does** contain state which affects its SQL
compilation is the one illustrated at :ref:`compilerext_compiling_subelements`;
this is an "INSERT FROM SELECT" construct that combines together a
:class:`_schema.Table` as well as a :class:`_sql.Select` construct, each of
which independently affect the SQL string generation of the construct.  For
this class, the example illustrates that it simply does not participate in
caching::

    class InsertFromSelect(Executable, ClauseElement):
        inherit_cache = False

        def __init__(self, table, select):
            self.table = table
            self.select = select

    @compiles(InsertFromSelect)
    def visit_insert_from_select(element, compiler, **kw):
        return "INSERT INTO %s (%s)" % (
            compiler.process(element.table, asfrom=True, **kw),
            compiler.process(element.select, **kw)
        )

While it is also possible that the above ``InsertFromSelect`` could be made to
produce a cache key that is composed of that of the :class:`_schema.Table` and
:class:`_sql.Select` components together, the API for this is not at the moment
fully public. However, for an "INSERT FROM SELECT" construct, which is only
used by itself for specific operations, caching is not as critical as in the
previous example.

For objects that are **used in relative isolation and are generally
standalone**, such as custom :term:`DML` constructs like an "INSERT FROM
SELECT", **caching is generally less critical** as the lack of caching for such
a construct will have only localized implications for that specific operation.


Further Examples
================

"UTC timestamp" function
-------------------------

A function that works like "CURRENT_TIMESTAMP" except applies the
appropriate conversions so that the time is in UTC time.   Timestamps are best
stored in relational databases as UTC, without time zones.   UTC so that your
database doesn't think time has gone backwards in the hour when daylight
savings ends, without timezones because timezones are like character
encodings - they're best applied only at the endpoints of an application
(i.e. convert to UTC upon user input, re-apply desired timezone upon display).

For PostgreSQL and Microsoft SQL Server::

    from sqlalchemy.sql import expression
    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.types import DateTime

    class utcnow(expression.FunctionElement):
        type = DateTime()
        inherit_cache = True

    @compiles(utcnow, 'postgresql')
    def pg_utcnow(element, compiler, **kw):
        return "TIMEZONE('utc', CURRENT_TIMESTAMP)"

    @compiles(utcnow, 'mssql')
    def ms_utcnow(element, compiler, **kw):
        return "GETUTCDATE()"

Example usage::

    from sqlalchemy import (
                Table, Column, Integer, String, DateTime, MetaData
            )
    metadata = MetaData()
    event = Table("event", metadata,
        Column("id", Integer, primary_key=True),
        Column("description", String(50), nullable=False),
        Column("timestamp", DateTime, server_default=utcnow())
    )

"GREATEST" function
-------------------

The "GREATEST" function is given any number of arguments and returns the one
that is of the highest value - its equivalent to Python's ``max``
function.  A SQL standard version versus a CASE based version which only
accommodates two arguments::

    from sqlalchemy.sql import expression, case
    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.types import Numeric

    class greatest(expression.FunctionElement):
        type = Numeric()
        name = 'greatest'
        inherit_cache = True

    @compiles(greatest)
    def default_greatest(element, compiler, **kw):
        return compiler.visit_function(element)

    @compiles(greatest, 'sqlite')
    @compiles(greatest, 'mssql')
    @compiles(greatest, 'oracle')
    def case_greatest(element, compiler, **kw):
        arg1, arg2 = list(element.clauses)
        return compiler.process(case([(arg1 > arg2, arg1)], else_=arg2), **kw)

Example usage::

    Session.query(Account).\
            filter(
                greatest(
                    Account.checking_balance,
                    Account.savings_balance) > 10000
            )

"false" expression
------------------

Render a "false" constant expression, rendering as "0" on platforms that
don't have a "false" constant::

    from sqlalchemy.sql import expression
    from sqlalchemy.ext.compiler import compiles

    class sql_false(expression.ColumnElement):
        inherit_cache = True

    @compiles(sql_false)
    def default_false(element, compiler, **kw):
        return "false"

    @compiles(sql_false, 'mssql')
    @compiles(sql_false, 'mysql')
    @compiles(sql_false, 'oracle')
    def int_false(element, compiler, **kw):
        return "0"

Example usage::

    from sqlalchemy import select, union_all

    exp = union_all(
        select(users.c.name, sql_false().label("enrolled")),
        select(customers.c.name, customers.c.enrolled)
    )

"""
from .. import exc
from ..sql import sqltypes


def compiles(class_, *specs):
    """Register a function as a compiler for a
    given :class:`_expression.ClauseElement` type."""

    def decorate(fn):
        # get an existing @compiles handler
        existing = class_.__dict__.get("_compiler_dispatcher", None)

        # get the original handler.  All ClauseElement classes have one
        # of these, but some TypeEngine classes will not.
        existing_dispatch = getattr(class_, "_compiler_dispatch", None)

        if not existing:
            existing = _dispatcher()

            if existing_dispatch:

                def _wrap_existing_dispatch(element, compiler, **kw):
                    try:
                        return existing_dispatch(element, compiler, **kw)
                    except exc.UnsupportedCompilationError as uce:
                        raise exc.UnsupportedCompilationError(
                            compiler,
                            type(element),
                            message="%s construct has no default "
                            "compilation handler." % type(element),
                        ) from uce

                existing.specs["default"] = _wrap_existing_dispatch

            # TODO: why is the lambda needed ?
            setattr(
                class_,
                "_compiler_dispatch",
                lambda *arg, **kw: existing(*arg, **kw),
            )
            setattr(class_, "_compiler_dispatcher", existing)

        if specs:
            for s in specs:
                existing.specs[s] = fn

        else:
            existing.specs["default"] = fn
        return fn

    return decorate


def deregister(class_):
    """Remove all custom compilers associated with a given
    :class:`_expression.ClauseElement` type.

    """

    if hasattr(class_, "_compiler_dispatcher"):
        class_._compiler_dispatch = class_._original_compiler_dispatch
        del class_._compiler_dispatcher


class _dispatcher:
    def __init__(self):
        self.specs = {}

    def __call__(self, element, compiler, **kw):
        # TODO: yes, this could also switch off of DBAPI in use.
        fn = self.specs.get(compiler.dialect.name, None)
        if not fn:
            try:
                fn = self.specs["default"]
            except KeyError as ke:
                raise exc.UnsupportedCompilationError(
                    compiler,
                    type(element),
                    message="%s construct has no default "
                    "compilation handler." % type(element),
                ) from ke

        # if compilation includes add_to_result_map, collect add_to_result_map
        # arguments from the user-defined callable, which are probably none
        # because this is not public API.  if it wasn't called, then call it
        # ourselves.
        arm = kw.get("add_to_result_map", None)
        if arm:
            arm_collection = []
            kw["add_to_result_map"] = lambda *args: arm_collection.append(args)

        expr = fn(element, compiler, **kw)

        if arm:
            if not arm_collection:
                arm_collection.append(
                    (None, None, (element,), sqltypes.NULLTYPE)
                )
            for tup in arm_collection:
                arm(*tup)
        return expr
