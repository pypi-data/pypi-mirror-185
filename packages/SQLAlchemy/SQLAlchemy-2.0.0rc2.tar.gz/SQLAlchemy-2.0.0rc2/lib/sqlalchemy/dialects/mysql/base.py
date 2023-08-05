# mysql/base.py
# Copyright (C) 2005-2023 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php
# mypy: ignore-errors


r"""

.. dialect:: mysql
    :name: MySQL / MariaDB
    :full_support: 5.6, 5.7, 8.0 / 10.4, 10.5
    :normal_support: 5.6+ / 10+
    :best_effort: 5.0.2+ / 5.0.2+

Supported Versions and Features
-------------------------------

SQLAlchemy supports MySQL starting with version 5.0.2 through modern releases,
as well as all modern versions of MariaDB.   See the official MySQL
documentation for detailed information about features supported in any given
server release.

.. versionchanged:: 1.4  minimum MySQL version supported is now 5.0.2.

MariaDB Support
~~~~~~~~~~~~~~~

The MariaDB variant of MySQL retains fundamental compatibility with MySQL's
protocols however the development of these two products continues to diverge.
Within the realm of SQLAlchemy, the two databases have a small number of
syntactical and behavioral differences that SQLAlchemy accommodates automatically.
To connect to a MariaDB database, no changes to the database URL are required::


    engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

Upon first connect, the SQLAlchemy dialect employs a
server version detection scheme that determines if the
backing database reports as MariaDB.  Based on this flag, the dialect
can make different choices in those of areas where its behavior
must be different.

.. _mysql_mariadb_only_mode:

MariaDB-Only Mode
~~~~~~~~~~~~~~~~~

The dialect also supports an **optional** "MariaDB-only" mode of connection, which may be
useful for the case where an application makes use of MariaDB-specific features
and is not compatible with a MySQL database.    To use this mode of operation,
replace the "mysql" token in the above URL with "mariadb"::

    engine = create_engine("mariadb+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

The above engine, upon first connect, will raise an error if the server version
detection detects that the backing database is not MariaDB.

When using an engine with ``"mariadb"`` as the dialect name, **all mysql-specific options
that include the name "mysql" in them are now named with "mariadb"**.  This means
options like ``mysql_engine`` should be named ``mariadb_engine``, etc.  Both
"mysql" and "mariadb" options can be used simultaneously for applications that
use URLs with both "mysql" and "mariadb" dialects::

    my_table = Table(
        "mytable",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("textdata", String(50)),
        mariadb_engine="InnoDB",
        mysql_engine="InnoDB",
    )

    Index(
        "textdata_ix",
        my_table.c.textdata,
        mysql_prefix="FULLTEXT",
        mariadb_prefix="FULLTEXT",
    )

Similar behavior will occur when the above structures are reflected, i.e. the
"mariadb" prefix will be present in the option names when the database URL
is based on the "mariadb" name.

.. versionadded:: 1.4 Added "mariadb" dialect name supporting "MariaDB-only mode"
   for the MySQL dialect.

.. _mysql_connection_timeouts:

Connection Timeouts and Disconnects
-----------------------------------

MySQL / MariaDB feature an automatic connection close behavior, for connections that
have been idle for a fixed period of time, defaulting to eight hours.
To circumvent having this issue, use
the :paramref:`_sa.create_engine.pool_recycle` option which ensures that
a connection will be discarded and replaced with a new one if it has been
present in the pool for a fixed number of seconds::

    engine = create_engine('mysql+mysqldb://...', pool_recycle=3600)

For more comprehensive disconnect detection of pooled connections, including
accommodation of  server restarts and network issues, a pre-ping approach may
be employed.  See :ref:`pool_disconnects` for current approaches.

.. seealso::

    :ref:`pool_disconnects` - Background on several techniques for dealing
    with timed out connections as well as database restarts.

.. _mysql_storage_engines:

CREATE TABLE arguments including Storage Engines
------------------------------------------------

Both MySQL's and MariaDB's CREATE TABLE syntax includes a wide array of special options,
including ``ENGINE``, ``CHARSET``, ``MAX_ROWS``, ``ROW_FORMAT``,
``INSERT_METHOD``, and many more.
To accommodate the rendering of these arguments, specify the form
``mysql_argument_name="value"``.  For example, to specify a table with
``ENGINE`` of ``InnoDB``, ``CHARSET`` of ``utf8mb4``, and ``KEY_BLOCK_SIZE``
of ``1024``::

  Table('mytable', metadata,
        Column('data', String(32)),
        mysql_engine='InnoDB',
        mysql_charset='utf8mb4',
        mysql_key_block_size="1024"
       )

When supporting :ref:`mysql_mariadb_only_mode` mode, similar keys against
the "mariadb" prefix must be included as well.  The values can of course
vary independently so that different settings on MySQL vs. MariaDB may
be maintained::

  # support both "mysql" and "mariadb-only" engine URLs

  Table('mytable', metadata,
        Column('data', String(32)),

        mysql_engine='InnoDB',
        mariadb_engine='InnoDB',

        mysql_charset='utf8mb4',
        mariadb_charset='utf8',

        mysql_key_block_size="1024"
        mariadb_key_block_size="1024"

       )

The MySQL / MariaDB dialects will normally transfer any keyword specified as
``mysql_keyword_name`` to be rendered as ``KEYWORD_NAME`` in the
``CREATE TABLE`` statement.  A handful of these names will render with a space
instead of an underscore; to support this, the MySQL dialect has awareness of
these particular names, which include ``DATA DIRECTORY``
(e.g. ``mysql_data_directory``), ``CHARACTER SET`` (e.g.
``mysql_character_set``) and ``INDEX DIRECTORY`` (e.g.
``mysql_index_directory``).

The most common argument is ``mysql_engine``, which refers to the storage
engine for the table.  Historically, MySQL server installations would default
to ``MyISAM`` for this value, although newer versions may be defaulting
to ``InnoDB``.  The ``InnoDB`` engine is typically preferred for its support
of transactions and foreign keys.

A :class:`_schema.Table`
that is created in a MySQL / MariaDB database with a storage engine
of ``MyISAM`` will be essentially non-transactional, meaning any
INSERT/UPDATE/DELETE statement referring to this table will be invoked as
autocommit.   It also will have no support for foreign key constraints; while
the ``CREATE TABLE`` statement accepts foreign key options, when using the
``MyISAM`` storage engine these arguments are discarded.  Reflecting such a
table will also produce no foreign key constraint information.

For fully atomic transactions as well as support for foreign key
constraints, all participating ``CREATE TABLE`` statements must specify a
transactional engine, which in the vast majority of cases is ``InnoDB``.


Case Sensitivity and Table Reflection
-------------------------------------

Both MySQL and MariaDB have inconsistent support for case-sensitive identifier
names, basing support on specific details of the underlying
operating system. However, it has been observed that no matter
what case sensitivity behavior is present, the names of tables in
foreign key declarations are *always* received from the database
as all-lower case, making it impossible to accurately reflect a
schema where inter-related tables use mixed-case identifier names.

Therefore it is strongly advised that table names be declared as
all lower case both within SQLAlchemy as well as on the MySQL / MariaDB
database itself, especially if database reflection features are
to be used.

.. _mysql_isolation_level:

Transaction Isolation Level
---------------------------

All MySQL / MariaDB dialects support setting of transaction isolation level both via a
dialect-specific parameter :paramref:`_sa.create_engine.isolation_level`
accepted
by :func:`_sa.create_engine`, as well as the
:paramref:`.Connection.execution_options.isolation_level` argument as passed to
:meth:`_engine.Connection.execution_options`.
This feature works by issuing the
command ``SET SESSION TRANSACTION ISOLATION LEVEL <level>`` for each new
connection.  For the special AUTOCOMMIT isolation level, DBAPI-specific
techniques are used.

To set isolation level using :func:`_sa.create_engine`::

    engine = create_engine(
                    "mysql+mysqldb://scott:tiger@localhost/test",
                    isolation_level="READ UNCOMMITTED"
                )

To set using per-connection execution options::

    connection = engine.connect()
    connection = connection.execution_options(
        isolation_level="READ COMMITTED"
    )

Valid values for ``isolation_level`` include:

* ``READ COMMITTED``
* ``READ UNCOMMITTED``
* ``REPEATABLE READ``
* ``SERIALIZABLE``
* ``AUTOCOMMIT``

The special ``AUTOCOMMIT`` value makes use of the various "autocommit"
attributes provided by specific DBAPIs, and is currently supported by
MySQLdb, MySQL-Client, MySQL-Connector Python, and PyMySQL.   Using it,
the database connection will return true for the value of
``SELECT @@autocommit;``.

There are also more options for isolation level configurations, such as
"sub-engine" objects linked to a main :class:`_engine.Engine` which each apply
different isolation level settings.  See the discussion at
:ref:`dbapi_autocommit` for background.

.. seealso::

    :ref:`dbapi_autocommit`

AUTO_INCREMENT Behavior
-----------------------

When creating tables, SQLAlchemy will automatically set ``AUTO_INCREMENT`` on
the first :class:`.Integer` primary key column which is not marked as a
foreign key::

  >>> t = Table('mytable', metadata,
  ...   Column('mytable_id', Integer, primary_key=True)
  ... )
  >>> t.create()
  CREATE TABLE mytable (
          id INTEGER NOT NULL AUTO_INCREMENT,
          PRIMARY KEY (id)
  )

You can disable this behavior by passing ``False`` to the
:paramref:`_schema.Column.autoincrement` argument of :class:`_schema.Column`.
This flag
can also be used to enable auto-increment on a secondary column in a
multi-column key for some storage engines::

  Table('mytable', metadata,
        Column('gid', Integer, primary_key=True, autoincrement=False),
        Column('id', Integer, primary_key=True)
       )

.. _mysql_ss_cursors:

Server Side Cursors
-------------------

Server-side cursor support is available for the mysqlclient, PyMySQL,
mariadbconnector dialects and may also be available in others.   This makes use
of either the "buffered=True/False" flag if available or by using a class such
as ``MySQLdb.cursors.SSCursor`` or ``pymysql.cursors.SSCursor`` internally.


Server side cursors are enabled on a per-statement basis by using the
:paramref:`.Connection.execution_options.stream_results` connection execution
option::

    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(text("select * from table"))

Note that some kinds of SQL statements may not be supported with
server side cursors; generally, only SQL statements that return rows should be
used with this option.

.. deprecated:: 1.4  The dialect-level server_side_cursors flag is deprecated
   and will be removed in a future release.  Please use the
   :paramref:`_engine.Connection.stream_results` execution option for
   unbuffered cursor support.

.. seealso::

    :ref:`engine_stream_results`

.. _mysql_unicode:

Unicode
-------

Charset Selection
~~~~~~~~~~~~~~~~~

Most MySQL / MariaDB DBAPIs offer the option to set the client character set for
a connection.   This is typically delivered using the ``charset`` parameter
in the URL, such as::

    e = create_engine(
        "mysql+pymysql://scott:tiger@localhost/test?charset=utf8mb4")

This charset is the **client character set** for the connection.  Some
MySQL DBAPIs will default this to a value such as ``latin1``, and some
will make use of the ``default-character-set`` setting in the ``my.cnf``
file as well.   Documentation for the DBAPI in use should be consulted
for specific behavior.

The encoding used for Unicode has traditionally been ``'utf8'``.  However, for
MySQL versions 5.5.3 and MariaDB 5.5 on forward, a new MySQL-specific encoding
``'utf8mb4'`` has been introduced, and as of MySQL 8.0 a warning is emitted by
the server if plain ``utf8`` is specified within any server-side directives,
replaced with ``utf8mb3``.  The rationale for this new encoding is due to the
fact that MySQL's legacy utf-8 encoding only supports codepoints up to three
bytes instead of four.  Therefore, when communicating with a MySQL or MariaDB
database that includes codepoints more than three bytes in size, this new
charset is preferred, if supported by both the database as well as the client
DBAPI, as in::

    e = create_engine(
        "mysql+pymysql://scott:tiger@localhost/test?charset=utf8mb4")

All modern DBAPIs should support the ``utf8mb4`` charset.

In order to use ``utf8mb4`` encoding for a schema that was created with  legacy
``utf8``, changes to the MySQL/MariaDB schema and/or server configuration may be
required.

.. seealso::

    `The utf8mb4 Character Set \
    <https://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html>`_ - \
    in the MySQL documentation

.. _mysql_binary_introducer:

Dealing with Binary Data Warnings and Unicode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL versions 5.6, 5.7 and later (not MariaDB at the time of this writing) now
emit a warning when attempting to pass binary data to the database, while a
character set encoding is also in place, when the binary data itself is not
valid for that encoding::

    default.py:509: Warning: (1300, "Invalid utf8mb4 character string:
    'F9876A'")
      cursor.execute(statement, parameters)

This warning is due to the fact that the MySQL client library is attempting to
interpret the binary string as a unicode object even if a datatype such
as :class:`.LargeBinary` is in use.   To resolve this, the SQL statement requires
a binary "character set introducer" be present before any non-NULL value
that renders like this::

    INSERT INTO table (data) VALUES (_binary %s)

These character set introducers are provided by the DBAPI driver, assuming the
use of mysqlclient or PyMySQL (both of which are recommended).  Add the query
string parameter ``binary_prefix=true`` to the URL to repair this warning::

    # mysqlclient
    engine = create_engine(
        "mysql+mysqldb://scott:tiger@localhost/test?charset=utf8mb4&binary_prefix=true")

    # PyMySQL
    engine = create_engine(
        "mysql+pymysql://scott:tiger@localhost/test?charset=utf8mb4&binary_prefix=true")


The ``binary_prefix`` flag may or may not be supported by other MySQL drivers.

SQLAlchemy itself cannot render this ``_binary`` prefix reliably, as it does
not work with the NULL value, which is valid to be sent as a bound parameter.
As the MySQL driver renders parameters directly into the SQL string, it's the
most efficient place for this additional keyword to be passed.

.. seealso::

    `Character set introducers <https://dev.mysql.com/doc/refman/5.7/en/charset-introducer.html>`_ - on the MySQL website


ANSI Quoting Style
------------------

MySQL / MariaDB feature two varieties of identifier "quoting style", one using
backticks and the other using quotes, e.g. ```some_identifier```  vs.
``"some_identifier"``.   All MySQL dialects detect which version
is in use by checking the value of :ref:`sql_mode<mysql_sql_mode>` when a connection is first
established with a particular :class:`_engine.Engine`.
This quoting style comes
into play when rendering table and column names as well as when reflecting
existing database structures.  The detection is entirely automatic and
no special configuration is needed to use either quoting style.


.. _mysql_sql_mode:

Changing the sql_mode
---------------------

MySQL supports operating in multiple
`Server SQL Modes <https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html>`_  for
both Servers and Clients. To change the ``sql_mode`` for a given application, a
developer can leverage SQLAlchemy's Events system.

In the following example, the event system is used to set the ``sql_mode`` on
the ``first_connect`` and ``connect`` events::

    from sqlalchemy import create_engine, event

    eng = create_engine("mysql+mysqldb://scott:tiger@localhost/test", echo='debug')

    # `insert=True` will ensure this is the very first listener to run
    @event.listens_for(eng, "connect", insert=True)
    def connect(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("SET sql_mode = 'STRICT_ALL_TABLES'")

    conn = eng.connect()

In the example illustrated above, the "connect" event will invoke the "SET"
statement on the connection at the moment a particular DBAPI connection is
first created for a given Pool, before the connection is made available to the
connection pool.  Additionally, because the function was registered with
``insert=True``, it will be prepended to the internal list of registered
functions.


MySQL / MariaDB SQL Extensions
------------------------------

Many of the MySQL / MariaDB SQL extensions are handled through SQLAlchemy's generic
function and operator support::

  table.select(table.c.password==func.md5('plaintext'))
  table.select(table.c.username.op('regexp')('^[a-d]'))

And of course any valid SQL statement can be executed as a string as well.

Some limited direct support for MySQL / MariaDB extensions to SQL is currently
available.

* INSERT..ON DUPLICATE KEY UPDATE:  See
  :ref:`mysql_insert_on_duplicate_key_update`

* SELECT pragma, use :meth:`_expression.Select.prefix_with` and
  :meth:`_query.Query.prefix_with`::

    select(...).prefix_with(['HIGH_PRIORITY', 'SQL_SMALL_RESULT'])

* UPDATE with LIMIT::

    update(..., mysql_limit=10, mariadb_limit=10)

* optimizer hints, use :meth:`_expression.Select.prefix_with` and
  :meth:`_query.Query.prefix_with`::

    select(...).prefix_with("/*+ NO_RANGE_OPTIMIZATION(t4 PRIMARY) */")

* index hints, use :meth:`_expression.Select.with_hint` and
  :meth:`_query.Query.with_hint`::

    select(...).with_hint(some_table, "USE INDEX xyz")

* MATCH operator support::

    from sqlalchemy.dialects.mysql import match
    select(...).where(match(col1, col2, against="some expr").in_boolean_mode())

    .. seealso::

        :class:`_mysql.match`

INSERT/DELETE...RETURNING
-------------------------

The MariaDB dialect supports 10.5+'s ``INSERT..RETURNING`` and
``DELETE..RETURNING`` (10.0+) syntaxes.   ``INSERT..RETURNING`` may be used
automatically in some cases in order to fetch newly generated identifiers in
place of the traditional approach of using ``cursor.lastrowid``, however
``cursor.lastrowid`` is currently still preferred for simple single-statement
cases for its better performance.

To specify an explicit ``RETURNING`` clause, use the
:meth:`._UpdateBase.returning` method on a per-statement basis::

    # INSERT..RETURNING
    result = connection.execute(
        table.insert().
        values(name='foo').
        returning(table.c.col1, table.c.col2)
    )
    print(result.all())

    # DELETE..RETURNING
    result = connection.execute(
        table.delete().
        where(table.c.name=='foo').
        returning(table.c.col1, table.c.col2)
    )
    print(result.all())

.. versionadded:: 2.0  Added support for MariaDB RETURNING

.. _mysql_insert_on_duplicate_key_update:

INSERT...ON DUPLICATE KEY UPDATE (Upsert)
------------------------------------------

MySQL / MariaDB allow "upserts" (update or insert)
of rows into a table via the ``ON DUPLICATE KEY UPDATE`` clause of the
``INSERT`` statement.  A candidate row will only be inserted if that row does
not match an existing primary or unique key in the table; otherwise, an UPDATE
will be performed.   The statement allows for separate specification of the
values to INSERT versus the values for UPDATE.

SQLAlchemy provides ``ON DUPLICATE KEY UPDATE`` support via the MySQL-specific
:func:`.mysql.insert()` function, which provides
the generative method :meth:`~.mysql.Insert.on_duplicate_key_update`:

.. sourcecode:: pycon+sql

    >>> from sqlalchemy.dialects.mysql import insert

    >>> insert_stmt = insert(my_table).values(
    ...     id='some_existing_id',
    ...     data='inserted value')

    >>> on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    ...     data=insert_stmt.inserted.data,
    ...     status='U'
    ... )
    >>> print(on_duplicate_key_stmt)
    {opensql}INSERT INTO my_table (id, data) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE data = VALUES(data), status = %s


Unlike PostgreSQL's "ON CONFLICT" phrase, the "ON DUPLICATE KEY UPDATE"
phrase will always match on any primary key or unique key, and will always
perform an UPDATE if there's a match; there are no options for it to raise
an error or to skip performing an UPDATE.

``ON DUPLICATE KEY UPDATE`` is used to perform an update of the already
existing row, using any combination of new values as well as values
from the proposed insertion.   These values are normally specified using
keyword arguments passed to the
:meth:`_mysql.Insert.on_duplicate_key_update`
given column key values (usually the name of the column, unless it
specifies :paramref:`_schema.Column.key`
) as keys and literal or SQL expressions
as values:

.. sourcecode:: pycon+sql

    >>> insert_stmt = insert(my_table).values(
    ...          id='some_existing_id',
    ...          data='inserted value')

    >>> on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    ...     data="some data",
    ...     updated_at=func.current_timestamp(),
    ... )

    >>> print(on_duplicate_key_stmt)
    {opensql}INSERT INTO my_table (id, data) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE data = %s, updated_at = CURRENT_TIMESTAMP

In a manner similar to that of :meth:`.UpdateBase.values`, other parameter
forms are accepted, including a single dictionary:

.. sourcecode:: pycon+sql

    >>> on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    ...     {"data": "some data", "updated_at": func.current_timestamp()},
    ... )

as well as a list of 2-tuples, which will automatically provide
a parameter-ordered UPDATE statement in a manner similar to that described
at :ref:`tutorial_parameter_ordered_updates`.  Unlike the :class:`_expression.Update`
object,
no special flag is needed to specify the intent since the argument form is
this context is unambiguous:

.. sourcecode:: pycon+sql

    >>> on_duplicate_key_stmt = insert_stmt.on_duplicate_key_update(
    ...     [
    ...         ("data", "some data"),
    ...         ("updated_at", func.current_timestamp()),
    ...     ]
    ... )

    >>> print(on_duplicate_key_stmt)
    {opensql}INSERT INTO my_table (id, data) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE data = %s, updated_at = CURRENT_TIMESTAMP

.. versionchanged:: 1.3 support for parameter-ordered UPDATE clause within
   MySQL ON DUPLICATE KEY UPDATE

.. warning::

    The :meth:`_mysql.Insert.on_duplicate_key_update`
    method does **not** take into
    account Python-side default UPDATE values or generation functions, e.g.
    e.g. those specified using :paramref:`_schema.Column.onupdate`.
    These values will not be exercised for an ON DUPLICATE KEY style of UPDATE,
    unless they are manually specified explicitly in the parameters.



In order to refer to the proposed insertion row, the special alias
:attr:`_mysql.Insert.inserted` is available as an attribute on
the :class:`_mysql.Insert` object; this object is a
:class:`_expression.ColumnCollection` which contains all columns of the target
table:

.. sourcecode:: pycon+sql

    >>> stmt = insert(my_table).values(
    ...     id='some_id',
    ...     data='inserted value',
    ...     author='jlh')

    >>> do_update_stmt = stmt.on_duplicate_key_update(
    ...     data="updated value",
    ...     author=stmt.inserted.author
    ... )

    >>> print(do_update_stmt)
    {opensql}INSERT INTO my_table (id, data, author) VALUES (%s, %s, %s)
    ON DUPLICATE KEY UPDATE data = %s, author = VALUES(author)

When rendered, the "inserted" namespace will produce the expression
``VALUES(<columnname>)``.

.. versionadded:: 1.2 Added support for MySQL ON DUPLICATE KEY UPDATE clause



rowcount Support
----------------

SQLAlchemy standardizes the DBAPI ``cursor.rowcount`` attribute to be the
usual definition of "number of rows matched by an UPDATE or DELETE" statement.
This is in contradiction to the default setting on most MySQL DBAPI drivers,
which is "number of rows actually modified/deleted".  For this reason, the
SQLAlchemy MySQL dialects always add the ``constants.CLIENT.FOUND_ROWS``
flag, or whatever is equivalent for the target dialect, upon connection.
This setting is currently hardcoded.

.. seealso::

    :attr:`_engine.CursorResult.rowcount`


.. _mysql_indexes:

MySQL / MariaDB- Specific Index Options
-----------------------------------------

MySQL and MariaDB-specific extensions to the :class:`.Index` construct are available.

Index Length
~~~~~~~~~~~~~

MySQL and MariaDB both provide an option to create index entries with a certain length, where
"length" refers to the number of characters or bytes in each value which will
become part of the index. SQLAlchemy provides this feature via the
``mysql_length`` and/or ``mariadb_length`` parameters::

    Index('my_index', my_table.c.data, mysql_length=10, mariadb_length=10)

    Index('a_b_idx', my_table.c.a, my_table.c.b, mysql_length={'a': 4,
                                                               'b': 9})

    Index('a_b_idx', my_table.c.a, my_table.c.b, mariadb_length={'a': 4,
                                                               'b': 9})

Prefix lengths are given in characters for nonbinary string types and in bytes
for binary string types. The value passed to the keyword argument *must* be
either an integer (and, thus, specify the same prefix length value for all
columns of the index) or a dict in which keys are column names and values are
prefix length values for corresponding columns. MySQL and MariaDB only allow a
length for a column of an index if it is for a CHAR, VARCHAR, TEXT, BINARY,
VARBINARY and BLOB.

Index Prefixes
~~~~~~~~~~~~~~

MySQL storage engines permit you to specify an index prefix when creating
an index. SQLAlchemy provides this feature via the
``mysql_prefix`` parameter on :class:`.Index`::

    Index('my_index', my_table.c.data, mysql_prefix='FULLTEXT')

The value passed to the keyword argument will be simply passed through to the
underlying CREATE INDEX, so it *must* be a valid index prefix for your MySQL
storage engine.

.. versionadded:: 1.1.5

.. seealso::

    `CREATE INDEX <https://dev.mysql.com/doc/refman/5.0/en/create-index.html>`_ - MySQL documentation

Index Types
~~~~~~~~~~~~~

Some MySQL storage engines permit you to specify an index type when creating
an index or primary key constraint. SQLAlchemy provides this feature via the
``mysql_using`` parameter on :class:`.Index`::

    Index('my_index', my_table.c.data, mysql_using='hash', mariadb_using='hash')

As well as the ``mysql_using`` parameter on :class:`.PrimaryKeyConstraint`::

    PrimaryKeyConstraint("data", mysql_using='hash', mariadb_using='hash')

The value passed to the keyword argument will be simply passed through to the
underlying CREATE INDEX or PRIMARY KEY clause, so it *must* be a valid index
type for your MySQL storage engine.

More information can be found at:

https://dev.mysql.com/doc/refman/5.0/en/create-index.html

https://dev.mysql.com/doc/refman/5.0/en/create-table.html

Index Parsers
~~~~~~~~~~~~~

CREATE FULLTEXT INDEX in MySQL also supports a "WITH PARSER" option.  This
is available using the keyword argument ``mysql_with_parser``::

    Index(
        'my_index', my_table.c.data,
        mysql_prefix='FULLTEXT', mysql_with_parser="ngram",
        mariadb_prefix='FULLTEXT', mariadb_with_parser="ngram",
    )

.. versionadded:: 1.3


.. _mysql_foreign_keys:

MySQL / MariaDB Foreign Keys
-----------------------------

MySQL and MariaDB's behavior regarding foreign keys has some important caveats.

Foreign Key Arguments to Avoid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Neither MySQL nor MariaDB support the foreign key arguments "DEFERRABLE", "INITIALLY",
or "MATCH".  Using the ``deferrable`` or ``initially`` keyword argument with
:class:`_schema.ForeignKeyConstraint` or :class:`_schema.ForeignKey`
will have the effect of
these keywords being rendered in a DDL expression, which will then raise an
error on MySQL or MariaDB.  In order to use these keywords on a foreign key while having
them ignored on a MySQL / MariaDB backend, use a custom compile rule::

    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.schema import ForeignKeyConstraint

    @compiles(ForeignKeyConstraint, "mysql", "mariadb")
    def process(element, compiler, **kw):
        element.deferrable = element.initially = None
        return compiler.visit_foreign_key_constraint(element, **kw)

The "MATCH" keyword is in fact more insidious, and is explicitly disallowed
by SQLAlchemy in conjunction with the MySQL or MariaDB backends.  This argument is
silently ignored by MySQL / MariaDB, but in addition has the effect of ON UPDATE and ON
DELETE options also being ignored by the backend.   Therefore MATCH should
never be used with the MySQL / MariaDB backends; as is the case with DEFERRABLE and
INITIALLY, custom compilation rules can be used to correct a
ForeignKeyConstraint at DDL definition time.

Reflection of Foreign Key Constraints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not all MySQL / MariaDB storage engines support foreign keys.  When using the
very common ``MyISAM`` MySQL storage engine, the information loaded by table
reflection will not include foreign keys.  For these tables, you may supply a
:class:`~sqlalchemy.ForeignKeyConstraint` at reflection time::

  Table('mytable', metadata,
        ForeignKeyConstraint(['other_id'], ['othertable.other_id']),
        autoload_with=engine
       )

.. seealso::

    :ref:`mysql_storage_engines`

.. _mysql_unique_constraints:

MySQL / MariaDB Unique Constraints and Reflection
----------------------------------------------------

SQLAlchemy supports both the :class:`.Index` construct with the
flag ``unique=True``, indicating a UNIQUE index, as well as the
:class:`.UniqueConstraint` construct, representing a UNIQUE constraint.
Both objects/syntaxes are supported by MySQL / MariaDB when emitting DDL to create
these constraints.  However, MySQL / MariaDB does not have a unique constraint
construct that is separate from a unique index; that is, the "UNIQUE"
constraint on MySQL / MariaDB is equivalent to creating a "UNIQUE INDEX".

When reflecting these constructs, the
:meth:`_reflection.Inspector.get_indexes`
and the :meth:`_reflection.Inspector.get_unique_constraints`
methods will **both**
return an entry for a UNIQUE index in MySQL / MariaDB.  However, when performing
full table reflection using ``Table(..., autoload_with=engine)``,
the :class:`.UniqueConstraint` construct is
**not** part of the fully reflected :class:`_schema.Table` construct under any
circumstances; this construct is always represented by a :class:`.Index`
with the ``unique=True`` setting present in the :attr:`_schema.Table.indexes`
collection.


TIMESTAMP / DATETIME issues
---------------------------

.. _mysql_timestamp_onupdate:

Rendering ON UPDATE CURRENT TIMESTAMP for MySQL / MariaDB's explicit_defaults_for_timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL / MariaDB have historically expanded the DDL for the :class:`_types.TIMESTAMP`
datatype into the phrase "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE
CURRENT_TIMESTAMP", which includes non-standard SQL that automatically updates
the column with the current timestamp when an UPDATE occurs, eliminating the
usual need to use a trigger in such a case where server-side update changes are
desired.

MySQL 5.6 introduced a new flag `explicit_defaults_for_timestamp
<https://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html
#sysvar_explicit_defaults_for_timestamp>`_ which disables the above behavior,
and in MySQL 8 this flag defaults to true, meaning in order to get a MySQL
"on update timestamp" without changing this flag, the above DDL must be
rendered explicitly.   Additionally, the same DDL is valid for use of the
``DATETIME`` datatype as well.

SQLAlchemy's MySQL dialect does not yet have an option to generate
MySQL's "ON UPDATE CURRENT_TIMESTAMP" clause, noting that this is not a general
purpose "ON UPDATE" as there is no such syntax in standard SQL.  SQLAlchemy's
:paramref:`_schema.Column.server_onupdate` parameter is currently not related
to this special MySQL behavior.

To generate this DDL, make use of the :paramref:`_schema.Column.server_default`
parameter and pass a textual clause that also includes the ON UPDATE clause::

    from sqlalchemy import Table, MetaData, Column, Integer, String, TIMESTAMP
    from sqlalchemy import text

    metadata = MetaData()

    mytable = Table(
        "mytable",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('data', String(50)),
        Column(
            'last_updated',
            TIMESTAMP,
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        )
    )

The same instructions apply to use of the :class:`_types.DateTime` and
:class:`_types.DATETIME` datatypes::

    from sqlalchemy import DateTime

    mytable = Table(
        "mytable",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('data', String(50)),
        Column(
            'last_updated',
            DateTime,
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        )
    )


Even though the :paramref:`_schema.Column.server_onupdate` feature does not
generate this DDL, it still may be desirable to signal to the ORM that this
updated value should be fetched.  This syntax looks like the following::

    from sqlalchemy.schema import FetchedValue

    class MyClass(Base):
        __tablename__ = 'mytable'

        id = Column(Integer, primary_key=True)
        data = Column(String(50))
        last_updated = Column(
            TIMESTAMP,
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            server_onupdate=FetchedValue()
        )


.. _mysql_timestamp_null:

TIMESTAMP Columns and NULL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MySQL historically enforces that a column which specifies the
TIMESTAMP datatype implicitly includes a default value of
CURRENT_TIMESTAMP, even though this is not stated, and additionally
sets the column as NOT NULL, the opposite behavior vs. that of all
other datatypes::

    mysql> CREATE TABLE ts_test (
        -> a INTEGER,
        -> b INTEGER NOT NULL,
        -> c TIMESTAMP,
        -> d TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        -> e TIMESTAMP NULL);
    Query OK, 0 rows affected (0.03 sec)

    mysql> SHOW CREATE TABLE ts_test;
    +---------+-----------------------------------------------------
    | Table   | Create Table
    +---------+-----------------------------------------------------
    | ts_test | CREATE TABLE `ts_test` (
      `a` int(11) DEFAULT NULL,
      `b` int(11) NOT NULL,
      `c` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      `d` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
      `e` timestamp NULL DEFAULT NULL
    ) ENGINE=MyISAM DEFAULT CHARSET=latin1

Above, we see that an INTEGER column defaults to NULL, unless it is specified
with NOT NULL.   But when the column is of type TIMESTAMP, an implicit
default of CURRENT_TIMESTAMP is generated which also coerces the column
to be a NOT NULL, even though we did not specify it as such.

This behavior of MySQL can be changed on the MySQL side using the
`explicit_defaults_for_timestamp
<https://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html
#sysvar_explicit_defaults_for_timestamp>`_ configuration flag introduced in
MySQL 5.6.  With this server setting enabled, TIMESTAMP columns behave like
any other datatype on the MySQL side with regards to defaults and nullability.

However, to accommodate the vast majority of MySQL databases that do not
specify this new flag, SQLAlchemy emits the "NULL" specifier explicitly with
any TIMESTAMP column that does not specify ``nullable=False``.   In order to
accommodate newer databases that specify ``explicit_defaults_for_timestamp``,
SQLAlchemy also emits NOT NULL for TIMESTAMP columns that do specify
``nullable=False``.   The following example illustrates::

    from sqlalchemy import MetaData, Integer, Table, Column, text
    from sqlalchemy.dialects.mysql import TIMESTAMP

    m = MetaData()
    t = Table('ts_test', m,
            Column('a', Integer),
            Column('b', Integer, nullable=False),
            Column('c', TIMESTAMP),
            Column('d', TIMESTAMP, nullable=False)
        )


    from sqlalchemy import create_engine
    e = create_engine("mysql+mysqldb://scott:tiger@localhost/test", echo=True)
    m.create_all(e)

output::

    CREATE TABLE ts_test (
        a INTEGER,
        b INTEGER NOT NULL,
        c TIMESTAMP NULL,
        d TIMESTAMP NOT NULL
    )

.. versionchanged:: 1.0.0 - SQLAlchemy now renders NULL or NOT NULL in all
   cases for TIMESTAMP columns, to accommodate
   ``explicit_defaults_for_timestamp``.  Prior to this version, it will
   not render "NOT NULL" for a TIMESTAMP column that is ``nullable=False``.

"""  # noqa

from array import array as _array
from collections import defaultdict
from itertools import compress
import re

from sqlalchemy import literal_column
from sqlalchemy.sql import visitors
from . import reflection as _reflection
from .enumerated import ENUM
from .enumerated import SET
from .json import JSON
from .json import JSONIndexType
from .json import JSONPathType
from .reserved_words import RESERVED_WORDS_MARIADB
from .reserved_words import RESERVED_WORDS_MYSQL
from .types import _FloatType
from .types import _IntegerType
from .types import _MatchType
from .types import _NumericType
from .types import _StringType
from .types import BIGINT
from .types import BIT
from .types import CHAR
from .types import DATETIME
from .types import DECIMAL
from .types import DOUBLE
from .types import FLOAT
from .types import INTEGER
from .types import LONGBLOB
from .types import LONGTEXT
from .types import MEDIUMBLOB
from .types import MEDIUMINT
from .types import MEDIUMTEXT
from .types import NCHAR
from .types import NUMERIC
from .types import NVARCHAR
from .types import REAL
from .types import SMALLINT
from .types import TEXT
from .types import TIME
from .types import TIMESTAMP
from .types import TINYBLOB
from .types import TINYINT
from .types import TINYTEXT
from .types import VARCHAR
from .types import YEAR
from ... import exc
from ... import log
from ... import schema as sa_schema
from ... import sql
from ... import util
from ...engine import default
from ...engine import reflection
from ...engine.reflection import ReflectionDefaults
from ...sql import coercions
from ...sql import compiler
from ...sql import elements
from ...sql import functions
from ...sql import operators
from ...sql import roles
from ...sql import sqltypes
from ...sql import util as sql_util
from ...types import BINARY
from ...types import BLOB
from ...types import BOOLEAN
from ...types import DATE
from ...types import VARBINARY
from ...util import topological

SET_RE = re.compile(
    r"\s*SET\s+(?:(?:GLOBAL|SESSION)\s+)?\w", re.I | re.UNICODE
)


# old names
MSTime = TIME
MSSet = SET
MSEnum = ENUM
MSLongBlob = LONGBLOB
MSMediumBlob = MEDIUMBLOB
MSTinyBlob = TINYBLOB
MSBlob = BLOB
MSBinary = BINARY
MSVarBinary = VARBINARY
MSNChar = NCHAR
MSNVarChar = NVARCHAR
MSChar = CHAR
MSString = VARCHAR
MSLongText = LONGTEXT
MSMediumText = MEDIUMTEXT
MSTinyText = TINYTEXT
MSText = TEXT
MSYear = YEAR
MSTimeStamp = TIMESTAMP
MSBit = BIT
MSSmallInteger = SMALLINT
MSTinyInteger = TINYINT
MSMediumInteger = MEDIUMINT
MSBigInteger = BIGINT
MSNumeric = NUMERIC
MSDecimal = DECIMAL
MSDouble = DOUBLE
MSReal = REAL
MSFloat = FLOAT
MSInteger = INTEGER

colspecs = {
    _IntegerType: _IntegerType,
    _NumericType: _NumericType,
    _FloatType: _FloatType,
    sqltypes.Numeric: NUMERIC,
    sqltypes.Float: FLOAT,
    sqltypes.Double: DOUBLE,
    sqltypes.Time: TIME,
    sqltypes.Enum: ENUM,
    sqltypes.MatchType: _MatchType,
    sqltypes.JSON: JSON,
    sqltypes.JSON.JSONIndexType: JSONIndexType,
    sqltypes.JSON.JSONPathType: JSONPathType,
}

# Everything 3.23 through 5.1 excepting OpenGIS types.
ischema_names = {
    "bigint": BIGINT,
    "binary": BINARY,
    "bit": BIT,
    "blob": BLOB,
    "boolean": BOOLEAN,
    "char": CHAR,
    "date": DATE,
    "datetime": DATETIME,
    "decimal": DECIMAL,
    "double": DOUBLE,
    "enum": ENUM,
    "fixed": DECIMAL,
    "float": FLOAT,
    "int": INTEGER,
    "integer": INTEGER,
    "json": JSON,
    "longblob": LONGBLOB,
    "longtext": LONGTEXT,
    "mediumblob": MEDIUMBLOB,
    "mediumint": MEDIUMINT,
    "mediumtext": MEDIUMTEXT,
    "nchar": NCHAR,
    "nvarchar": NVARCHAR,
    "numeric": NUMERIC,
    "set": SET,
    "smallint": SMALLINT,
    "text": TEXT,
    "time": TIME,
    "timestamp": TIMESTAMP,
    "tinyblob": TINYBLOB,
    "tinyint": TINYINT,
    "tinytext": TINYTEXT,
    "varbinary": VARBINARY,
    "varchar": VARCHAR,
    "year": YEAR,
}


class MySQLExecutionContext(default.DefaultExecutionContext):
    def create_server_side_cursor(self):
        if self.dialect.supports_server_side_cursors:
            return self._dbapi_connection.cursor(self.dialect._sscursor)
        else:
            raise NotImplementedError()

    def fire_sequence(self, seq, type_):
        return self._execute_scalar(
            (
                "select nextval(%s)"
                % self.identifier_preparer.format_sequence(seq)
            ),
            type_,
        )


class MySQLCompiler(compiler.SQLCompiler):

    render_table_with_column_in_update_from = True
    """Overridden from base SQLCompiler value"""

    extract_map = compiler.SQLCompiler.extract_map.copy()
    extract_map.update({"milliseconds": "millisecond"})

    def default_from(self):
        """Called when a ``SELECT`` statement has no froms,
        and no ``FROM`` clause is to be appended.

        """
        if self.stack:
            stmt = self.stack[-1]["selectable"]
            if stmt._where_criteria:
                return " FROM DUAL"

        return ""

    def visit_random_func(self, fn, **kw):
        return "rand%s" % self.function_argspec(fn)

    def visit_rollup_func(self, fn, **kw):
        clause = ", ".join(
            elem._compiler_dispatch(self, **kw) for elem in fn.clauses
        )
        return f"{clause} WITH ROLLUP"

    def visit_sequence(self, seq, **kw):
        return "nextval(%s)" % self.preparer.format_sequence(seq)

    def visit_sysdate_func(self, fn, **kw):
        return "SYSDATE()"

    def _render_json_extract_from_binary(self, binary, operator, **kw):
        # note we are intentionally calling upon the process() calls in the
        # order in which they appear in the SQL String as this is used
        # by positional parameter rendering

        if binary.type._type_affinity is sqltypes.JSON:
            return "JSON_EXTRACT(%s, %s)" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
            )

        # for non-JSON, MySQL doesn't handle JSON null at all so it has to
        # be explicit
        case_expression = "CASE JSON_EXTRACT(%s, %s) WHEN 'null' THEN NULL" % (
            self.process(binary.left, **kw),
            self.process(binary.right, **kw),
        )

        if binary.type._type_affinity is sqltypes.Integer:
            type_expression = (
                "ELSE CAST(JSON_EXTRACT(%s, %s) AS SIGNED INTEGER)"
                % (
                    self.process(binary.left, **kw),
                    self.process(binary.right, **kw),
                )
            )
        elif binary.type._type_affinity is sqltypes.Numeric:
            if (
                binary.type.scale is not None
                and binary.type.precision is not None
            ):
                # using DECIMAL here because MySQL does not recognize NUMERIC
                type_expression = (
                    "ELSE CAST(JSON_EXTRACT(%s, %s) AS DECIMAL(%s, %s))"
                    % (
                        self.process(binary.left, **kw),
                        self.process(binary.right, **kw),
                        binary.type.precision,
                        binary.type.scale,
                    )
                )
            else:
                # FLOAT / REAL not added in MySQL til 8.0.17
                type_expression = (
                    "ELSE JSON_EXTRACT(%s, %s)+0.0000000000000000000000"
                    % (
                        self.process(binary.left, **kw),
                        self.process(binary.right, **kw),
                    )
                )
        elif binary.type._type_affinity is sqltypes.Boolean:
            # the NULL handling is particularly weird with boolean, so
            # explicitly return true/false constants
            type_expression = "WHEN true THEN true ELSE false"
        elif binary.type._type_affinity is sqltypes.String:
            # (gord): this fails with a JSON value that's a four byte unicode
            # string.  SQLite has the same problem at the moment
            # (zzzeek): I'm not really sure.  let's take a look at a test case
            # that hits each backend and maybe make a requires rule for it?
            type_expression = "ELSE JSON_UNQUOTE(JSON_EXTRACT(%s, %s))" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
            )
        else:
            # other affinity....this is not expected right now
            type_expression = "ELSE JSON_EXTRACT(%s, %s)" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
            )

        return case_expression + " " + type_expression + " END"

    def visit_json_getitem_op_binary(self, binary, operator, **kw):
        return self._render_json_extract_from_binary(binary, operator, **kw)

    def visit_json_path_getitem_op_binary(self, binary, operator, **kw):
        return self._render_json_extract_from_binary(binary, operator, **kw)

    def visit_on_duplicate_key_update(self, on_duplicate, **kw):
        statement = self.current_executable

        if on_duplicate._parameter_ordering:
            parameter_ordering = [
                coercions.expect(roles.DMLColumnRole, key)
                for key in on_duplicate._parameter_ordering
            ]
            ordered_keys = set(parameter_ordering)
            cols = [
                statement.table.c[key]
                for key in parameter_ordering
                if key in statement.table.c
            ] + [c for c in statement.table.c if c.key not in ordered_keys]
        else:
            cols = statement.table.c

        clauses = []
        # traverses through all table columns to preserve table column order
        for column in (col for col in cols if col.key in on_duplicate.update):

            val = on_duplicate.update[column.key]

            if coercions._is_literal(val):
                val = elements.BindParameter(None, val, type_=column.type)
                value_text = self.process(val.self_group(), use_schema=False)
            else:

                def replace(obj):
                    if (
                        isinstance(obj, elements.BindParameter)
                        and obj.type._isnull
                    ):
                        obj = obj._clone()
                        obj.type = column.type
                        return obj
                    elif (
                        isinstance(obj, elements.ColumnClause)
                        and obj.table is on_duplicate.inserted_alias
                    ):
                        obj = literal_column(
                            "VALUES(" + self.preparer.quote(obj.name) + ")"
                        )
                        return obj
                    else:
                        # element is not replaced
                        return None

                val = visitors.replacement_traverse(val, {}, replace)
                value_text = self.process(val.self_group(), use_schema=False)

            name_text = self.preparer.quote(column.name)
            clauses.append("%s = %s" % (name_text, value_text))

        non_matching = set(on_duplicate.update) - {c.key for c in cols}
        if non_matching:
            util.warn(
                "Additional column names not matching "
                "any column keys in table '%s': %s"
                % (
                    self.statement.table.name,
                    (", ".join("'%s'" % c for c in non_matching)),
                )
            )

        return "ON DUPLICATE KEY UPDATE " + ", ".join(clauses)

    def visit_concat_op_expression_clauselist(
        self, clauselist, operator, **kw
    ):
        return "concat(%s)" % (
            ", ".join(self.process(elem, **kw) for elem in clauselist.clauses)
        )

    def visit_concat_op_binary(self, binary, operator, **kw):
        return "concat(%s, %s)" % (
            self.process(binary.left, **kw),
            self.process(binary.right, **kw),
        )

    _match_valid_flag_combinations = frozenset(
        (
            # (boolean_mode, natural_language, query_expansion)
            (False, False, False),
            (True, False, False),
            (False, True, False),
            (False, False, True),
            (False, True, True),
        )
    )

    _match_flag_expressions = (
        "IN BOOLEAN MODE",
        "IN NATURAL LANGUAGE MODE",
        "WITH QUERY EXPANSION",
    )

    def visit_mysql_match(self, element, **kw):
        return self.visit_match_op_binary(element, element.operator, **kw)

    def visit_match_op_binary(self, binary, operator, **kw):
        """
        Note that `mysql_boolean_mode` is enabled by default because of
        backward compatibility
        """

        modifiers = binary.modifiers

        boolean_mode = modifiers.get("mysql_boolean_mode", True)
        natural_language = modifiers.get("mysql_natural_language", False)
        query_expansion = modifiers.get("mysql_query_expansion", False)

        flag_combination = (boolean_mode, natural_language, query_expansion)

        if flag_combination not in self._match_valid_flag_combinations:
            flags = (
                "in_boolean_mode=%s" % boolean_mode,
                "in_natural_language_mode=%s" % natural_language,
                "with_query_expansion=%s" % query_expansion,
            )

            flags = ", ".join(flags)

            raise exc.CompileError("Invalid MySQL match flags: %s" % flags)

        match_clause = binary.left
        match_clause = self.process(match_clause, **kw)
        against_clause = self.process(binary.right, **kw)

        if any(flag_combination):
            flag_expressions = compress(
                self._match_flag_expressions,
                flag_combination,
            )

            against_clause = [against_clause]
            against_clause.extend(flag_expressions)

            against_clause = " ".join(against_clause)

        return "MATCH (%s) AGAINST (%s)" % (match_clause, against_clause)

    def get_from_hint_text(self, table, text):
        return text

    def visit_typeclause(self, typeclause, type_=None, **kw):
        if type_ is None:
            type_ = typeclause.type.dialect_impl(self.dialect)
        if isinstance(type_, sqltypes.TypeDecorator):
            return self.visit_typeclause(typeclause, type_.impl, **kw)
        elif isinstance(type_, sqltypes.Integer):
            if getattr(type_, "unsigned", False):
                return "UNSIGNED INTEGER"
            else:
                return "SIGNED INTEGER"
        elif isinstance(type_, sqltypes.TIMESTAMP):
            return "DATETIME"
        elif isinstance(
            type_,
            (
                sqltypes.DECIMAL,
                sqltypes.DateTime,
                sqltypes.Date,
                sqltypes.Time,
            ),
        ):
            return self.dialect.type_compiler_instance.process(type_)
        elif isinstance(type_, sqltypes.String) and not isinstance(
            type_, (ENUM, SET)
        ):
            adapted = CHAR._adapt_string_for_cast(type_)
            return self.dialect.type_compiler_instance.process(adapted)
        elif isinstance(type_, sqltypes._Binary):
            return "BINARY"
        elif isinstance(type_, sqltypes.JSON):
            return "JSON"
        elif isinstance(type_, sqltypes.NUMERIC):
            return self.dialect.type_compiler_instance.process(type_).replace(
                "NUMERIC", "DECIMAL"
            )
        elif (
            isinstance(type_, sqltypes.Float)
            and self.dialect._support_float_cast
        ):
            return self.dialect.type_compiler_instance.process(type_)
        else:
            return None

    def visit_cast(self, cast, **kw):
        type_ = self.process(cast.typeclause)
        if type_ is None:
            util.warn(
                "Datatype %s does not support CAST on MySQL/MariaDb; "
                "the CAST will be skipped."
                % self.dialect.type_compiler_instance.process(
                    cast.typeclause.type
                )
            )
            return self.process(cast.clause.self_group(), **kw)

        return "CAST(%s AS %s)" % (self.process(cast.clause, **kw), type_)

    def render_literal_value(self, value, type_):
        value = super().render_literal_value(value, type_)
        if self.dialect._backslash_escapes:
            value = value.replace("\\", "\\\\")
        return value

    # override native_boolean=False behavior here, as
    # MySQL still supports native boolean
    def visit_true(self, element, **kw):
        return "true"

    def visit_false(self, element, **kw):
        return "false"

    def get_select_precolumns(self, select, **kw):
        """Add special MySQL keywords in place of DISTINCT.

        .. deprecated 1.4:: this usage is deprecated.
           :meth:`_expression.Select.prefix_with` should be used for special
           keywords at the start of a SELECT.

        """
        if isinstance(select._distinct, str):
            util.warn_deprecated(
                "Sending string values for 'distinct' is deprecated in the "
                "MySQL dialect and will be removed in a future release.  "
                "Please use :meth:`.Select.prefix_with` for special keywords "
                "at the start of a SELECT statement",
                version="1.4",
            )
            return select._distinct.upper() + " "

        return super().get_select_precolumns(select, **kw)

    def visit_join(self, join, asfrom=False, from_linter=None, **kwargs):
        if from_linter:
            from_linter.edges.add((join.left, join.right))

        if join.full:
            join_type = " FULL OUTER JOIN "
        elif join.isouter:
            join_type = " LEFT OUTER JOIN "
        else:
            join_type = " INNER JOIN "

        return "".join(
            (
                self.process(
                    join.left, asfrom=True, from_linter=from_linter, **kwargs
                ),
                join_type,
                self.process(
                    join.right, asfrom=True, from_linter=from_linter, **kwargs
                ),
                " ON ",
                self.process(join.onclause, from_linter=from_linter, **kwargs),
            )
        )

    def for_update_clause(self, select, **kw):
        if select._for_update_arg.read:
            tmp = " LOCK IN SHARE MODE"
        else:
            tmp = " FOR UPDATE"

        if select._for_update_arg.of and self.dialect.supports_for_update_of:

            tables = util.OrderedSet()
            for c in select._for_update_arg.of:
                tables.update(sql_util.surface_selectables_only(c))

            tmp += " OF " + ", ".join(
                self.process(table, ashint=True, use_schema=False, **kw)
                for table in tables
            )

        if select._for_update_arg.nowait:
            tmp += " NOWAIT"

        if select._for_update_arg.skip_locked:
            tmp += " SKIP LOCKED"

        return tmp

    def limit_clause(self, select, **kw):
        # MySQL supports:
        #   LIMIT <limit>
        #   LIMIT <offset>, <limit>
        # and in server versions > 3.3:
        #   LIMIT <limit> OFFSET <offset>
        # The latter is more readable for offsets but we're stuck with the
        # former until we can refine dialects by server revision.

        limit_clause, offset_clause = (
            select._limit_clause,
            select._offset_clause,
        )

        if limit_clause is None and offset_clause is None:
            return ""
        elif offset_clause is not None:
            # As suggested by the MySQL docs, need to apply an
            # artificial limit if one wasn't provided
            # https://dev.mysql.com/doc/refman/5.0/en/select.html
            if limit_clause is None:
                # TODO: remove ??
                # hardwire the upper limit.  Currently
                # needed consistent with the usage of the upper
                # bound as part of MySQL's "syntax" for OFFSET with
                # no LIMIT.
                return " \n LIMIT %s, %s" % (
                    self.process(offset_clause, **kw),
                    "18446744073709551615",
                )
            else:
                return " \n LIMIT %s, %s" % (
                    self.process(offset_clause, **kw),
                    self.process(limit_clause, **kw),
                )
        else:
            # No offset provided, so just use the limit
            return " \n LIMIT %s" % (self.process(limit_clause, **kw),)

    def update_limit_clause(self, update_stmt):
        limit = update_stmt.kwargs.get("%s_limit" % self.dialect.name, None)
        if limit:
            return "LIMIT %s" % limit
        else:
            return None

    def update_tables_clause(self, update_stmt, from_table, extra_froms, **kw):
        kw["asfrom"] = True
        return ", ".join(
            t._compiler_dispatch(self, **kw)
            for t in [from_table] + list(extra_froms)
        )

    def update_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        return None

    def delete_table_clause(self, delete_stmt, from_table, extra_froms):
        """If we have extra froms make sure we render any alias as hint."""
        ashint = False
        if extra_froms:
            ashint = True
        return from_table._compiler_dispatch(
            self, asfrom=True, iscrud=True, ashint=ashint
        )

    def delete_extra_from_clause(
        self, delete_stmt, from_table, extra_froms, from_hints, **kw
    ):
        """Render the DELETE .. USING clause specific to MySQL."""
        kw["asfrom"] = True
        return "USING " + ", ".join(
            t._compiler_dispatch(self, fromhints=from_hints, **kw)
            for t in [from_table] + extra_froms
        )

    def visit_empty_set_expr(self, element_types, **kw):
        return (
            "SELECT %(outer)s FROM (SELECT %(inner)s) "
            "as _empty_set WHERE 1!=1"
            % {
                "inner": ", ".join(
                    "1 AS _in_%s" % idx
                    for idx, type_ in enumerate(element_types)
                ),
                "outer": ", ".join(
                    "_in_%s" % idx for idx, type_ in enumerate(element_types)
                ),
            }
        )

    def visit_is_distinct_from_binary(self, binary, operator, **kw):
        return "NOT (%s <=> %s)" % (
            self.process(binary.left),
            self.process(binary.right),
        )

    def visit_is_not_distinct_from_binary(self, binary, operator, **kw):
        return "%s <=> %s" % (
            self.process(binary.left),
            self.process(binary.right),
        )

    def _mariadb_regexp_flags(self, flags, pattern, **kw):
        return "CONCAT('(?', %s, ')', %s)" % (
            self.process(flags, **kw),
            self.process(pattern, **kw),
        )

    def _regexp_match(self, op_string, binary, operator, **kw):
        flags = binary.modifiers["flags"]
        if flags is None:
            return self._generate_generic_binary(binary, op_string, **kw)
        elif self.dialect.is_mariadb:
            return "%s%s%s" % (
                self.process(binary.left, **kw),
                op_string,
                self._mariadb_regexp_flags(flags, binary.right),
            )
        else:
            text = "REGEXP_LIKE(%s, %s, %s)" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
                self.process(flags, **kw),
            )
            if op_string == " NOT REGEXP ":
                return "NOT %s" % text
            else:
                return text

    def visit_regexp_match_op_binary(self, binary, operator, **kw):
        return self._regexp_match(" REGEXP ", binary, operator, **kw)

    def visit_not_regexp_match_op_binary(self, binary, operator, **kw):
        return self._regexp_match(" NOT REGEXP ", binary, operator, **kw)

    def visit_regexp_replace_op_binary(self, binary, operator, **kw):
        flags = binary.modifiers["flags"]
        replacement = binary.modifiers["replacement"]
        if flags is None:
            return "REGEXP_REPLACE(%s, %s, %s)" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
                self.process(replacement, **kw),
            )
        elif self.dialect.is_mariadb:
            return "REGEXP_REPLACE(%s, %s, %s)" % (
                self.process(binary.left, **kw),
                self._mariadb_regexp_flags(flags, binary.right),
                self.process(replacement, **kw),
            )
        else:
            return "REGEXP_REPLACE(%s, %s, %s, %s)" % (
                self.process(binary.left, **kw),
                self.process(binary.right, **kw),
                self.process(replacement, **kw),
                self.process(flags, **kw),
            )


class MySQLDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column, **kw):
        """Builds column DDL."""

        colspec = [
            self.preparer.format_column(column),
            self.dialect.type_compiler_instance.process(
                column.type, type_expression=column
            ),
        ]

        if column.computed is not None:
            colspec.append(self.process(column.computed))

        is_timestamp = isinstance(
            column.type._unwrapped_dialect_impl(self.dialect),
            sqltypes.TIMESTAMP,
        )

        if not column.nullable:
            colspec.append("NOT NULL")

        # see: https://docs.sqlalchemy.org/en/latest/dialects/mysql.html#mysql_timestamp_null  # noqa
        elif column.nullable and is_timestamp:
            colspec.append("NULL")

        comment = column.comment
        if comment is not None:
            literal = self.sql_compiler.render_literal_value(
                comment, sqltypes.String()
            )
            colspec.append("COMMENT " + literal)

        if (
            column.table is not None
            and column is column.table._autoincrement_column
            and (
                column.server_default is None
                or isinstance(column.server_default, sa_schema.Identity)
            )
            and not (
                self.dialect.supports_sequences
                and isinstance(column.default, sa_schema.Sequence)
                and not column.default.optional
            )
        ):
            colspec.append("AUTO_INCREMENT")
        else:
            default = self.get_column_default_string(column)
            if default is not None:
                colspec.append("DEFAULT " + default)
        return " ".join(colspec)

    def post_create_table(self, table):
        """Build table-level CREATE options like ENGINE and COLLATE."""

        table_opts = []

        opts = {
            k[len(self.dialect.name) + 1 :].upper(): v
            for k, v in table.kwargs.items()
            if k.startswith("%s_" % self.dialect.name)
        }

        if table.comment is not None:
            opts["COMMENT"] = table.comment

        partition_options = [
            "PARTITION_BY",
            "PARTITIONS",
            "SUBPARTITIONS",
            "SUBPARTITION_BY",
        ]

        nonpart_options = set(opts).difference(partition_options)
        part_options = set(opts).intersection(partition_options)

        for opt in topological.sort(
            [
                ("DEFAULT_CHARSET", "COLLATE"),
                ("DEFAULT_CHARACTER_SET", "COLLATE"),
                ("CHARSET", "COLLATE"),
                ("CHARACTER_SET", "COLLATE"),
            ],
            nonpart_options,
        ):
            arg = opts[opt]
            if opt in _reflection._options_of_type_string:

                arg = self.sql_compiler.render_literal_value(
                    arg, sqltypes.String()
                )

            if opt in (
                "DATA_DIRECTORY",
                "INDEX_DIRECTORY",
                "DEFAULT_CHARACTER_SET",
                "CHARACTER_SET",
                "DEFAULT_CHARSET",
                "DEFAULT_COLLATE",
            ):
                opt = opt.replace("_", " ")

            joiner = "="
            if opt in (
                "TABLESPACE",
                "DEFAULT CHARACTER SET",
                "CHARACTER SET",
                "COLLATE",
            ):
                joiner = " "

            table_opts.append(joiner.join((opt, arg)))

        for opt in topological.sort(
            [
                ("PARTITION_BY", "PARTITIONS"),
                ("PARTITION_BY", "SUBPARTITION_BY"),
                ("PARTITION_BY", "SUBPARTITIONS"),
                ("PARTITIONS", "SUBPARTITIONS"),
                ("PARTITIONS", "SUBPARTITION_BY"),
                ("SUBPARTITION_BY", "SUBPARTITIONS"),
            ],
            part_options,
        ):
            arg = opts[opt]
            if opt in _reflection._options_of_type_string:
                arg = self.sql_compiler.render_literal_value(
                    arg, sqltypes.String()
                )

            opt = opt.replace("_", " ")
            joiner = " "

            table_opts.append(joiner.join((opt, arg)))

        return " ".join(table_opts)

    def visit_create_index(self, create, **kw):
        index = create.element
        self._verify_index_table(index)
        preparer = self.preparer
        table = preparer.format_table(index.table)

        columns = [
            self.sql_compiler.process(
                elements.Grouping(expr)
                if (
                    isinstance(expr, elements.BinaryExpression)
                    or (
                        isinstance(expr, elements.UnaryExpression)
                        and expr.modifier
                        not in (operators.desc_op, operators.asc_op)
                    )
                    or isinstance(expr, functions.FunctionElement)
                )
                else expr,
                include_table=False,
                literal_binds=True,
            )
            for expr in index.expressions
        ]

        name = self._prepared_index_name(index)

        text = "CREATE "
        if index.unique:
            text += "UNIQUE "

        index_prefix = index.kwargs.get("%s_prefix" % self.dialect.name, None)
        if index_prefix:
            text += index_prefix + " "

        text += "INDEX "
        if create.if_not_exists:
            text += "IF NOT EXISTS "
        text += "%s ON %s " % (name, table)

        length = index.dialect_options[self.dialect.name]["length"]
        if length is not None:

            if isinstance(length, dict):
                # length value can be a (column_name --> integer value)
                # mapping specifying the prefix length for each column of the
                # index
                columns = ", ".join(
                    "%s(%d)" % (expr, length[col.name])
                    if col.name in length
                    else (
                        "%s(%d)" % (expr, length[expr])
                        if expr in length
                        else "%s" % expr
                    )
                    for col, expr in zip(index.expressions, columns)
                )
            else:
                # or can be an integer value specifying the same
                # prefix length for all columns of the index
                columns = ", ".join(
                    "%s(%d)" % (col, length) for col in columns
                )
        else:
            columns = ", ".join(columns)
        text += "(%s)" % columns

        parser = index.dialect_options["mysql"]["with_parser"]
        if parser is not None:
            text += " WITH PARSER %s" % (parser,)

        using = index.dialect_options["mysql"]["using"]
        if using is not None:
            text += " USING %s" % (preparer.quote(using))

        return text

    def visit_primary_key_constraint(self, constraint, **kw):
        text = super().visit_primary_key_constraint(constraint)
        using = constraint.dialect_options["mysql"]["using"]
        if using:
            text += " USING %s" % (self.preparer.quote(using))
        return text

    def visit_drop_index(self, drop, **kw):
        index = drop.element
        text = "\nDROP INDEX "
        if drop.if_exists:
            text += "IF EXISTS "

        return text + "%s ON %s" % (
            self._prepared_index_name(index, include_schema=False),
            self.preparer.format_table(index.table),
        )

    def visit_drop_constraint(self, drop, **kw):
        constraint = drop.element
        if isinstance(constraint, sa_schema.ForeignKeyConstraint):
            qual = "FOREIGN KEY "
            const = self.preparer.format_constraint(constraint)
        elif isinstance(constraint, sa_schema.PrimaryKeyConstraint):
            qual = "PRIMARY KEY "
            const = ""
        elif isinstance(constraint, sa_schema.UniqueConstraint):
            qual = "INDEX "
            const = self.preparer.format_constraint(constraint)
        elif isinstance(constraint, sa_schema.CheckConstraint):
            if self.dialect.is_mariadb:
                qual = "CONSTRAINT "
            else:
                qual = "CHECK "
            const = self.preparer.format_constraint(constraint)
        else:
            qual = ""
            const = self.preparer.format_constraint(constraint)
        return "ALTER TABLE %s DROP %s%s" % (
            self.preparer.format_table(constraint.table),
            qual,
            const,
        )

    def define_constraint_match(self, constraint):
        if constraint.match is not None:
            raise exc.CompileError(
                "MySQL ignores the 'MATCH' keyword while at the same time "
                "causes ON UPDATE/ON DELETE clauses to be ignored."
            )
        return ""

    def visit_set_table_comment(self, create, **kw):
        return "ALTER TABLE %s COMMENT %s" % (
            self.preparer.format_table(create.element),
            self.sql_compiler.render_literal_value(
                create.element.comment, sqltypes.String()
            ),
        )

    def visit_drop_table_comment(self, create, **kw):
        return "ALTER TABLE %s COMMENT ''" % (
            self.preparer.format_table(create.element)
        )

    def visit_set_column_comment(self, create, **kw):
        return "ALTER TABLE %s CHANGE %s %s" % (
            self.preparer.format_table(create.element.table),
            self.preparer.format_column(create.element),
            self.get_column_specification(create.element),
        )


class MySQLTypeCompiler(compiler.GenericTypeCompiler):
    def _extend_numeric(self, type_, spec):
        "Extend a numeric-type declaration with MySQL specific extensions."

        if not self._mysql_type(type_):
            return spec

        if type_.unsigned:
            spec += " UNSIGNED"
        if type_.zerofill:
            spec += " ZEROFILL"
        return spec

    def _extend_string(self, type_, defaults, spec):
        """Extend a string-type declaration with standard SQL CHARACTER SET /
        COLLATE annotations and MySQL specific extensions.

        """

        def attr(name):
            return getattr(type_, name, defaults.get(name))

        if attr("charset"):
            charset = "CHARACTER SET %s" % attr("charset")
        elif attr("ascii"):
            charset = "ASCII"
        elif attr("unicode"):
            charset = "UNICODE"
        else:
            charset = None

        if attr("collation"):
            collation = "COLLATE %s" % type_.collation
        elif attr("binary"):
            collation = "BINARY"
        else:
            collation = None

        if attr("national"):
            # NATIONAL (aka NCHAR/NVARCHAR) trumps charsets.
            return " ".join(
                [c for c in ("NATIONAL", spec, collation) if c is not None]
            )
        return " ".join(
            [c for c in (spec, charset, collation) if c is not None]
        )

    def _mysql_type(self, type_):
        return isinstance(type_, (_StringType, _NumericType))

    def visit_NUMERIC(self, type_, **kw):
        if type_.precision is None:
            return self._extend_numeric(type_, "NUMERIC")
        elif type_.scale is None:
            return self._extend_numeric(
                type_,
                "NUMERIC(%(precision)s)" % {"precision": type_.precision},
            )
        else:
            return self._extend_numeric(
                type_,
                "NUMERIC(%(precision)s, %(scale)s)"
                % {"precision": type_.precision, "scale": type_.scale},
            )

    def visit_DECIMAL(self, type_, **kw):
        if type_.precision is None:
            return self._extend_numeric(type_, "DECIMAL")
        elif type_.scale is None:
            return self._extend_numeric(
                type_,
                "DECIMAL(%(precision)s)" % {"precision": type_.precision},
            )
        else:
            return self._extend_numeric(
                type_,
                "DECIMAL(%(precision)s, %(scale)s)"
                % {"precision": type_.precision, "scale": type_.scale},
            )

    def visit_DOUBLE(self, type_, **kw):
        if type_.precision is not None and type_.scale is not None:
            return self._extend_numeric(
                type_,
                "DOUBLE(%(precision)s, %(scale)s)"
                % {"precision": type_.precision, "scale": type_.scale},
            )
        else:
            return self._extend_numeric(type_, "DOUBLE")

    def visit_REAL(self, type_, **kw):
        if type_.precision is not None and type_.scale is not None:
            return self._extend_numeric(
                type_,
                "REAL(%(precision)s, %(scale)s)"
                % {"precision": type_.precision, "scale": type_.scale},
            )
        else:
            return self._extend_numeric(type_, "REAL")

    def visit_FLOAT(self, type_, **kw):
        if (
            self._mysql_type(type_)
            and type_.scale is not None
            and type_.precision is not None
        ):
            return self._extend_numeric(
                type_, "FLOAT(%s, %s)" % (type_.precision, type_.scale)
            )
        elif type_.precision is not None:
            return self._extend_numeric(
                type_, "FLOAT(%s)" % (type_.precision,)
            )
        else:
            return self._extend_numeric(type_, "FLOAT")

    def visit_INTEGER(self, type_, **kw):
        if self._mysql_type(type_) and type_.display_width is not None:
            return self._extend_numeric(
                type_,
                "INTEGER(%(display_width)s)"
                % {"display_width": type_.display_width},
            )
        else:
            return self._extend_numeric(type_, "INTEGER")

    def visit_BIGINT(self, type_, **kw):
        if self._mysql_type(type_) and type_.display_width is not None:
            return self._extend_numeric(
                type_,
                "BIGINT(%(display_width)s)"
                % {"display_width": type_.display_width},
            )
        else:
            return self._extend_numeric(type_, "BIGINT")

    def visit_MEDIUMINT(self, type_, **kw):
        if self._mysql_type(type_) and type_.display_width is not None:
            return self._extend_numeric(
                type_,
                "MEDIUMINT(%(display_width)s)"
                % {"display_width": type_.display_width},
            )
        else:
            return self._extend_numeric(type_, "MEDIUMINT")

    def visit_TINYINT(self, type_, **kw):
        if self._mysql_type(type_) and type_.display_width is not None:
            return self._extend_numeric(
                type_, "TINYINT(%s)" % type_.display_width
            )
        else:
            return self._extend_numeric(type_, "TINYINT")

    def visit_SMALLINT(self, type_, **kw):
        if self._mysql_type(type_) and type_.display_width is not None:
            return self._extend_numeric(
                type_,
                "SMALLINT(%(display_width)s)"
                % {"display_width": type_.display_width},
            )
        else:
            return self._extend_numeric(type_, "SMALLINT")

    def visit_BIT(self, type_, **kw):
        if type_.length is not None:
            return "BIT(%s)" % type_.length
        else:
            return "BIT"

    def visit_DATETIME(self, type_, **kw):
        if getattr(type_, "fsp", None):
            return "DATETIME(%d)" % type_.fsp
        else:
            return "DATETIME"

    def visit_DATE(self, type_, **kw):
        return "DATE"

    def visit_TIME(self, type_, **kw):
        if getattr(type_, "fsp", None):
            return "TIME(%d)" % type_.fsp
        else:
            return "TIME"

    def visit_TIMESTAMP(self, type_, **kw):
        if getattr(type_, "fsp", None):
            return "TIMESTAMP(%d)" % type_.fsp
        else:
            return "TIMESTAMP"

    def visit_YEAR(self, type_, **kw):
        if type_.display_width is None:
            return "YEAR"
        else:
            return "YEAR(%s)" % type_.display_width

    def visit_TEXT(self, type_, **kw):
        if type_.length:
            return self._extend_string(type_, {}, "TEXT(%d)" % type_.length)
        else:
            return self._extend_string(type_, {}, "TEXT")

    def visit_TINYTEXT(self, type_, **kw):
        return self._extend_string(type_, {}, "TINYTEXT")

    def visit_MEDIUMTEXT(self, type_, **kw):
        return self._extend_string(type_, {}, "MEDIUMTEXT")

    def visit_LONGTEXT(self, type_, **kw):
        return self._extend_string(type_, {}, "LONGTEXT")

    def visit_VARCHAR(self, type_, **kw):
        if type_.length:
            return self._extend_string(type_, {}, "VARCHAR(%d)" % type_.length)
        else:
            raise exc.CompileError(
                "VARCHAR requires a length on dialect %s" % self.dialect.name
            )

    def visit_CHAR(self, type_, **kw):
        if type_.length:
            return self._extend_string(
                type_, {}, "CHAR(%(length)s)" % {"length": type_.length}
            )
        else:
            return self._extend_string(type_, {}, "CHAR")

    def visit_NVARCHAR(self, type_, **kw):
        # We'll actually generate the equiv. "NATIONAL VARCHAR" instead
        # of "NVARCHAR".
        if type_.length:
            return self._extend_string(
                type_,
                {"national": True},
                "VARCHAR(%(length)s)" % {"length": type_.length},
            )
        else:
            raise exc.CompileError(
                "NVARCHAR requires a length on dialect %s" % self.dialect.name
            )

    def visit_NCHAR(self, type_, **kw):
        # We'll actually generate the equiv.
        # "NATIONAL CHAR" instead of "NCHAR".
        if type_.length:
            return self._extend_string(
                type_,
                {"national": True},
                "CHAR(%(length)s)" % {"length": type_.length},
            )
        else:
            return self._extend_string(type_, {"national": True}, "CHAR")

    def visit_UUID(self, type_, **kw):
        return "UUID"

    def visit_VARBINARY(self, type_, **kw):
        return "VARBINARY(%d)" % type_.length

    def visit_JSON(self, type_, **kw):
        return "JSON"

    def visit_large_binary(self, type_, **kw):
        return self.visit_BLOB(type_)

    def visit_enum(self, type_, **kw):
        if not type_.native_enum:
            return super().visit_enum(type_)
        else:
            return self._visit_enumerated_values("ENUM", type_, type_.enums)

    def visit_BLOB(self, type_, **kw):
        if type_.length:
            return "BLOB(%d)" % type_.length
        else:
            return "BLOB"

    def visit_TINYBLOB(self, type_, **kw):
        return "TINYBLOB"

    def visit_MEDIUMBLOB(self, type_, **kw):
        return "MEDIUMBLOB"

    def visit_LONGBLOB(self, type_, **kw):
        return "LONGBLOB"

    def _visit_enumerated_values(self, name, type_, enumerated_values):
        quoted_enums = []
        for e in enumerated_values:
            quoted_enums.append("'%s'" % e.replace("'", "''"))
        return self._extend_string(
            type_, {}, "%s(%s)" % (name, ",".join(quoted_enums))
        )

    def visit_ENUM(self, type_, **kw):
        return self._visit_enumerated_values("ENUM", type_, type_.enums)

    def visit_SET(self, type_, **kw):
        return self._visit_enumerated_values("SET", type_, type_.values)

    def visit_BOOLEAN(self, type_, **kw):
        return "BOOL"


class MySQLIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words = RESERVED_WORDS_MYSQL

    def __init__(self, dialect, server_ansiquotes=False, **kw):
        if not server_ansiquotes:
            quote = "`"
        else:
            quote = '"'

        super().__init__(dialect, initial_quote=quote, escape_quote=quote)

    def _quote_free_identifiers(self, *ids):
        """Unilaterally identifier-quote any number of strings."""

        return tuple([self.quote_identifier(i) for i in ids if i is not None])


class MariaDBIdentifierPreparer(MySQLIdentifierPreparer):
    reserved_words = RESERVED_WORDS_MARIADB


@log.class_logger
class MySQLDialect(default.DefaultDialect):
    """Details of the MySQL dialect.
    Not used directly in application code.
    """

    name = "mysql"
    supports_statement_cache = True

    supports_alter = True

    # MySQL has no true "boolean" type; we
    # allow for the "true" and "false" keywords, however
    supports_native_boolean = False

    # identifiers are 64, however aliases can be 255...
    max_identifier_length = 255
    max_index_name_length = 64
    max_constraint_name_length = 64

    div_is_floordiv = False

    supports_native_enum = True

    supports_sequences = False  # default for MySQL ...
    # ... may be updated to True for MariaDB 10.3+ in initialize()

    sequences_optional = False

    supports_for_update_of = False  # default for MySQL ...
    # ... may be updated to True for MySQL 8+ in initialize()

    # MySQL doesn't support "DEFAULT VALUES" but *does* support
    # "VALUES (DEFAULT)"
    supports_default_values = False
    supports_default_metavalue = True

    use_insertmanyvalues: bool = True

    supports_sane_rowcount = True
    supports_sane_multi_rowcount = False
    supports_multivalues_insert = True
    insert_null_pk_still_autoincrements = True

    supports_comments = True
    inline_comments = True
    default_paramstyle = "format"
    colspecs = colspecs

    cte_follows_insert = True

    statement_compiler = MySQLCompiler
    ddl_compiler = MySQLDDLCompiler
    type_compiler_cls = MySQLTypeCompiler
    ischema_names = ischema_names
    preparer = MySQLIdentifierPreparer

    is_mariadb = False
    _mariadb_normalized_version_info = None

    # default SQL compilation settings -
    # these are modified upon initialize(),
    # i.e. first connect
    _backslash_escapes = True
    _server_ansiquotes = False

    construct_arguments = [
        (sa_schema.Table, {"*": None}),
        (sql.Update, {"limit": None}),
        (sa_schema.PrimaryKeyConstraint, {"using": None}),
        (
            sa_schema.Index,
            {
                "using": None,
                "length": None,
                "prefix": None,
                "with_parser": None,
            },
        ),
    ]

    def __init__(
        self,
        json_serializer=None,
        json_deserializer=None,
        is_mariadb=None,
        **kwargs,
    ):
        kwargs.pop("use_ansiquotes", None)  # legacy
        default.DefaultDialect.__init__(self, **kwargs)
        self._json_serializer = json_serializer
        self._json_deserializer = json_deserializer
        self._set_mariadb(is_mariadb, None)

    def get_isolation_level_values(self, dbapi_conn):
        return (
            "SERIALIZABLE",
            "READ UNCOMMITTED",
            "READ COMMITTED",
            "REPEATABLE READ",
        )

    def set_isolation_level(self, dbapi_connection, level):
        cursor = dbapi_connection.cursor()
        cursor.execute(f"SET SESSION TRANSACTION ISOLATION LEVEL {level}")
        cursor.execute("COMMIT")
        cursor.close()

    def get_isolation_level(self, dbapi_connection):
        cursor = dbapi_connection.cursor()
        if self._is_mysql and self.server_version_info >= (5, 7, 20):
            cursor.execute("SELECT @@transaction_isolation")
        else:
            cursor.execute("SELECT @@tx_isolation")
        row = cursor.fetchone()
        if row is None:
            util.warn(
                "Could not retrieve transaction isolation level for MySQL "
                "connection."
            )
            raise NotImplementedError()
        val = row[0]
        cursor.close()
        if isinstance(val, bytes):
            val = val.decode()
        return val.upper().replace("-", " ")

    @classmethod
    def _is_mariadb_from_url(cls, url):
        dbapi = cls.import_dbapi()
        dialect = cls(dbapi=dbapi)

        cargs, cparams = dialect.create_connect_args(url)
        conn = dialect.connect(*cargs, **cparams)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT VERSION() LIKE '%MariaDB%'")
            val = cursor.fetchone()[0]
        except:
            raise
        else:
            return bool(val)
        finally:
            conn.close()

    def _get_server_version_info(self, connection):
        # get database server version info explicitly over the wire
        # to avoid proxy servers like MaxScale getting in the
        # way with their own values, see #4205
        dbapi_con = connection.connection
        cursor = dbapi_con.cursor()
        cursor.execute("SELECT VERSION()")
        val = cursor.fetchone()[0]
        cursor.close()
        if isinstance(val, bytes):
            val = val.decode()

        return self._parse_server_version(val)

    def _parse_server_version(self, val):
        version = []
        is_mariadb = False

        r = re.compile(r"[.\-+]")
        tokens = r.split(val)
        for token in tokens:
            parsed_token = re.match(
                r"^(?:(\d+)(?:a|b|c)?|(MariaDB\w*))$", token
            )
            if not parsed_token:
                continue
            elif parsed_token.group(2):
                self._mariadb_normalized_version_info = tuple(version[-3:])
                is_mariadb = True
            else:
                digit = int(parsed_token.group(1))
                version.append(digit)

        server_version_info = tuple(version)

        self._set_mariadb(
            server_version_info and is_mariadb, server_version_info
        )

        if not is_mariadb:
            self._mariadb_normalized_version_info = server_version_info

        if server_version_info < (5, 0, 2):
            raise NotImplementedError(
                "the MySQL/MariaDB dialect supports server "
                "version info 5.0.2 and above."
            )

        # setting it here to help w the test suite
        self.server_version_info = server_version_info
        return server_version_info

    def _set_mariadb(self, is_mariadb, server_version_info):
        if is_mariadb is None:
            return

        if not is_mariadb and self.is_mariadb:
            raise exc.InvalidRequestError(
                "MySQL version %s is not a MariaDB variant."
                % (".".join(map(str, server_version_info)),)
            )
        if is_mariadb:
            self.preparer = MariaDBIdentifierPreparer
            # this would have been set by the default dialect already,
            # so set it again
            self.identifier_preparer = self.preparer(self)

            # this will be updated on first connect in initialize()
            # if using older mariadb version
            self.delete_returning = True
            self.insert_returning = True

        self.is_mariadb = is_mariadb

    def do_begin_twophase(self, connection, xid):
        connection.execute(sql.text("XA BEGIN :xid"), dict(xid=xid))

    def do_prepare_twophase(self, connection, xid):
        connection.execute(sql.text("XA END :xid"), dict(xid=xid))
        connection.execute(sql.text("XA PREPARE :xid"), dict(xid=xid))

    def do_rollback_twophase(
        self, connection, xid, is_prepared=True, recover=False
    ):
        if not is_prepared:
            connection.execute(sql.text("XA END :xid"), dict(xid=xid))
        connection.execute(sql.text("XA ROLLBACK :xid"), dict(xid=xid))

    def do_commit_twophase(
        self, connection, xid, is_prepared=True, recover=False
    ):
        if not is_prepared:
            self.do_prepare_twophase(connection, xid)
        connection.execute(sql.text("XA COMMIT :xid"), dict(xid=xid))

    def do_recover_twophase(self, connection):
        resultset = connection.exec_driver_sql("XA RECOVER")
        return [row["data"][0 : row["gtrid_length"]] for row in resultset]

    def is_disconnect(self, e, connection, cursor):
        if isinstance(
            e,
            (
                self.dbapi.OperationalError,
                self.dbapi.ProgrammingError,
                self.dbapi.InterfaceError,
            ),
        ) and self._extract_error_code(e) in (
            1927,
            2006,
            2013,
            2014,
            2045,
            2055,
            4031,
        ):
            return True
        elif isinstance(
            e, (self.dbapi.InterfaceError, self.dbapi.InternalError)
        ):
            # if underlying connection is closed,
            # this is the error you get
            return "(0, '')" in str(e)
        else:
            return False

    def _compat_fetchall(self, rp, charset=None):
        """Proxy result rows to smooth over MySQL-Python driver
        inconsistencies."""

        return [_DecodingRow(row, charset) for row in rp.fetchall()]

    def _compat_fetchone(self, rp, charset=None):
        """Proxy a result row to smooth over MySQL-Python driver
        inconsistencies."""

        row = rp.fetchone()
        if row:
            return _DecodingRow(row, charset)
        else:
            return None

    def _compat_first(self, rp, charset=None):
        """Proxy a result row to smooth over MySQL-Python driver
        inconsistencies."""

        row = rp.first()
        if row:
            return _DecodingRow(row, charset)
        else:
            return None

    def _extract_error_code(self, exception):
        raise NotImplementedError()

    def _get_default_schema_name(self, connection):
        return connection.exec_driver_sql("SELECT DATABASE()").scalar()

    @reflection.cache
    def has_table(self, connection, table_name, schema=None, **kw):
        self._ensure_has_table_connection(connection)

        if schema is None:
            schema = self.default_schema_name

        assert schema is not None

        full_name = ".".join(
            self.identifier_preparer._quote_free_identifiers(
                schema, table_name
            )
        )

        # DESCRIBE *must* be used because there is no information schema
        # table that returns information on temp tables that is consistently
        # available on MariaDB / MySQL / engine-agnostic etc.
        # therefore we have no choice but to use DESCRIBE and an error catch
        # to detect "False".  See issue #9058

        try:
            with connection.exec_driver_sql(
                f"DESCRIBE {full_name}",
                execution_options={"skip_user_error_events": True},
            ) as rs:
                return rs.fetchone() is not None
        except exc.DBAPIError as e:
            if self._extract_error_code(e.orig) == 1146:
                return False
            raise

    @reflection.cache
    def has_sequence(self, connection, sequence_name, schema=None, **kw):
        if not self.supports_sequences:
            self._sequences_not_supported()
        if not schema:
            schema = self.default_schema_name
        # MariaDB implements sequences as a special type of table
        #
        cursor = connection.execute(
            sql.text(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES "
                "WHERE TABLE_TYPE='SEQUENCE' and TABLE_NAME=:name AND "
                "TABLE_SCHEMA=:schema_name"
            ),
            dict(
                name=str(sequence_name),
                schema_name=str(schema),
            ),
        )
        return cursor.first() is not None

    def _sequences_not_supported(self):
        raise NotImplementedError(
            "Sequences are supported only by the "
            "MariaDB series 10.3 or greater"
        )

    @reflection.cache
    def get_sequence_names(self, connection, schema=None, **kw):
        if not self.supports_sequences:
            self._sequences_not_supported()
        if not schema:
            schema = self.default_schema_name
        # MariaDB implements sequences as a special type of table
        cursor = connection.execute(
            sql.text(
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES "
                "WHERE TABLE_TYPE='SEQUENCE' and TABLE_SCHEMA=:schema_name"
            ),
            dict(schema_name=schema),
        )
        return [
            row[0]
            for row in self._compat_fetchall(
                cursor, charset=self._connection_charset
            )
        ]

    def initialize(self, connection):
        # this is driver-based, does not need server version info
        # and is fairly critical for even basic SQL operations
        self._connection_charset = self._detect_charset(connection)

        # call super().initialize() because we need to have
        # server_version_info set up.  in 1.4 under python 2 only this does the
        # "check unicode returns" thing, which is the one area that some
        # SQL gets compiled within initialize() currently
        default.DefaultDialect.initialize(self, connection)

        self._detect_sql_mode(connection)
        self._detect_ansiquotes(connection)  # depends on sql mode
        self._detect_casing(connection)
        if self._server_ansiquotes:
            # if ansiquotes == True, build a new IdentifierPreparer
            # with the new setting
            self.identifier_preparer = self.preparer(
                self, server_ansiquotes=self._server_ansiquotes
            )

        self.supports_sequences = (
            self.is_mariadb and self.server_version_info >= (10, 3)
        )

        self.supports_for_update_of = (
            self._is_mysql and self.server_version_info >= (8,)
        )

        self._needs_correct_for_88718_96365 = (
            not self.is_mariadb and self.server_version_info >= (8,)
        )

        self.delete_returning = (
            self.is_mariadb and self.server_version_info >= (10, 0, 5)
        )

        self.insert_returning = (
            self.is_mariadb and self.server_version_info >= (10, 5)
        )

        self._warn_for_known_db_issues()

    def _warn_for_known_db_issues(self):
        if self.is_mariadb:
            mdb_version = self._mariadb_normalized_version_info
            if mdb_version > (10, 2) and mdb_version < (10, 2, 9):
                util.warn(
                    "MariaDB %r before 10.2.9 has known issues regarding "
                    "CHECK constraints, which impact handling of NULL values "
                    "with SQLAlchemy's boolean datatype (MDEV-13596). An "
                    "additional issue prevents proper migrations of columns "
                    "with CHECK constraints (MDEV-11114).  Please upgrade to "
                    "MariaDB 10.2.9 or greater, or use the MariaDB 10.1 "
                    "series, to avoid these issues." % (mdb_version,)
                )

    @property
    def _support_float_cast(self):
        if not self.server_version_info:
            return False
        elif self.is_mariadb:
            # ref https://mariadb.com/kb/en/mariadb-1045-release-notes/
            return self.server_version_info >= (10, 4, 5)
        else:
            # ref https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-17.html#mysqld-8-0-17-feature  # noqa
            return self.server_version_info >= (8, 0, 17)

    @property
    def _is_mariadb(self):
        return self.is_mariadb

    @property
    def _is_mysql(self):
        return not self.is_mariadb

    @property
    def _is_mariadb_102(self):
        return self.is_mariadb and self._mariadb_normalized_version_info > (
            10,
            2,
        )

    @reflection.cache
    def get_schema_names(self, connection, **kw):
        rp = connection.exec_driver_sql("SHOW schemas")
        return [r[0] for r in rp]

    @reflection.cache
    def get_table_names(self, connection, schema=None, **kw):
        """Return a Unicode SHOW TABLES from a given schema."""
        if schema is not None:
            current_schema = schema
        else:
            current_schema = self.default_schema_name

        charset = self._connection_charset

        rp = connection.exec_driver_sql(
            "SHOW FULL TABLES FROM %s"
            % self.identifier_preparer.quote_identifier(current_schema)
        )

        return [
            row[0]
            for row in self._compat_fetchall(rp, charset=charset)
            if row[1] == "BASE TABLE"
        ]

    @reflection.cache
    def get_view_names(self, connection, schema=None, **kw):
        if schema is None:
            schema = self.default_schema_name
        charset = self._connection_charset
        rp = connection.exec_driver_sql(
            "SHOW FULL TABLES FROM %s"
            % self.identifier_preparer.quote_identifier(schema)
        )
        return [
            row[0]
            for row in self._compat_fetchall(rp, charset=charset)
            if row[1] in ("VIEW", "SYSTEM VIEW")
        ]

    @reflection.cache
    def get_table_options(self, connection, table_name, schema=None, **kw):

        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )
        if parsed_state.table_options:
            return parsed_state.table_options
        else:
            return ReflectionDefaults.table_options()

    @reflection.cache
    def get_columns(self, connection, table_name, schema=None, **kw):
        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )
        if parsed_state.columns:
            return parsed_state.columns
        else:
            return ReflectionDefaults.columns()

    @reflection.cache
    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )
        for key in parsed_state.keys:
            if key["type"] == "PRIMARY":
                # There can be only one.
                cols = [s[0] for s in key["columns"]]
                return {"constrained_columns": cols, "name": None}
        return ReflectionDefaults.pk_constraint()

    @reflection.cache
    def get_foreign_keys(self, connection, table_name, schema=None, **kw):

        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )
        default_schema = None

        fkeys = []

        for spec in parsed_state.fk_constraints:
            ref_name = spec["table"][-1]
            ref_schema = len(spec["table"]) > 1 and spec["table"][-2] or schema

            if not ref_schema:
                if default_schema is None:
                    default_schema = connection.dialect.default_schema_name
                if schema == default_schema:
                    ref_schema = schema

            loc_names = spec["local"]
            ref_names = spec["foreign"]

            con_kw = {}
            for opt in ("onupdate", "ondelete"):
                if spec.get(opt, False) not in ("NO ACTION", None):
                    con_kw[opt] = spec[opt]

            fkey_d = {
                "name": spec["name"],
                "constrained_columns": loc_names,
                "referred_schema": ref_schema,
                "referred_table": ref_name,
                "referred_columns": ref_names,
                "options": con_kw,
            }
            fkeys.append(fkey_d)

        if self._needs_correct_for_88718_96365:
            self._correct_for_mysql_bugs_88718_96365(fkeys, connection)

        return fkeys if fkeys else ReflectionDefaults.foreign_keys()

    def _correct_for_mysql_bugs_88718_96365(self, fkeys, connection):
        # Foreign key is always in lower case (MySQL 8.0)
        # https://bugs.mysql.com/bug.php?id=88718
        # issue #4344 for SQLAlchemy

        # table name also for MySQL 8.0
        # https://bugs.mysql.com/bug.php?id=96365
        # issue #4751 for SQLAlchemy

        # for lower_case_table_names=2, information_schema.columns
        # preserves the original table/schema casing, but SHOW CREATE
        # TABLE does not.   this problem is not in lower_case_table_names=1,
        # but use case-insensitive matching for these two modes in any case.

        if self._casing in (1, 2):

            def lower(s):
                return s.lower()

        else:
            # if on case sensitive, there can be two tables referenced
            # with the same name different casing, so we need to use
            # case-sensitive matching.
            def lower(s):
                return s

        default_schema_name = connection.dialect.default_schema_name
        col_tuples = [
            (
                lower(rec["referred_schema"] or default_schema_name),
                lower(rec["referred_table"]),
                col_name,
            )
            for rec in fkeys
            for col_name in rec["referred_columns"]
        ]

        if col_tuples:

            correct_for_wrong_fk_case = connection.execute(
                sql.text(
                    """
                    select table_schema, table_name, column_name
                    from information_schema.columns
                    where (table_schema, table_name, lower(column_name)) in
                    :table_data;
                """
                ).bindparams(sql.bindparam("table_data", expanding=True)),
                dict(table_data=col_tuples),
            )

            # in casing=0, table name and schema name come back in their
            # exact case.
            # in casing=1, table name and schema name come back in lower
            # case.
            # in casing=2, table name and schema name come back from the
            # information_schema.columns view in the case
            # that was used in CREATE DATABASE and CREATE TABLE, but
            # SHOW CREATE TABLE converts them to *lower case*, therefore
            # not matching.  So for this case, case-insensitive lookup
            # is necessary
            d = defaultdict(dict)
            for schema, tname, cname in correct_for_wrong_fk_case:
                d[(lower(schema), lower(tname))]["SCHEMANAME"] = schema
                d[(lower(schema), lower(tname))]["TABLENAME"] = tname
                d[(lower(schema), lower(tname))][cname.lower()] = cname

            for fkey in fkeys:
                rec = d[
                    (
                        lower(fkey["referred_schema"] or default_schema_name),
                        lower(fkey["referred_table"]),
                    )
                ]

                fkey["referred_table"] = rec["TABLENAME"]
                if fkey["referred_schema"] is not None:
                    fkey["referred_schema"] = rec["SCHEMANAME"]

                fkey["referred_columns"] = [
                    rec[col.lower()] for col in fkey["referred_columns"]
                ]

    @reflection.cache
    def get_check_constraints(self, connection, table_name, schema=None, **kw):
        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )

        cks = [
            {"name": spec["name"], "sqltext": spec["sqltext"]}
            for spec in parsed_state.ck_constraints
        ]
        cks.sort(key=lambda d: d["name"] or "~")  # sort None as last
        return cks if cks else ReflectionDefaults.check_constraints()

    @reflection.cache
    def get_table_comment(self, connection, table_name, schema=None, **kw):
        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )
        comment = parsed_state.table_options.get(f"{self.name}_comment", None)
        if comment is not None:
            return {"text": comment}
        else:
            return ReflectionDefaults.table_comment()

    @reflection.cache
    def get_indexes(self, connection, table_name, schema=None, **kw):

        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )

        indexes = []

        for spec in parsed_state.keys:
            dialect_options = {}
            unique = False
            flavor = spec["type"]
            if flavor == "PRIMARY":
                continue
            if flavor == "UNIQUE":
                unique = True
            elif flavor in ("FULLTEXT", "SPATIAL"):
                dialect_options["%s_prefix" % self.name] = flavor
            elif flavor is None:
                pass
            else:
                self.logger.info(
                    "Converting unknown KEY type %s to a plain KEY", flavor
                )
                pass

            if spec["parser"]:
                dialect_options["%s_with_parser" % (self.name)] = spec[
                    "parser"
                ]

            index_d = {}

            index_d["name"] = spec["name"]
            index_d["column_names"] = [s[0] for s in spec["columns"]]
            mysql_length = {
                s[0]: s[1] for s in spec["columns"] if s[1] is not None
            }
            if mysql_length:
                dialect_options["%s_length" % self.name] = mysql_length

            index_d["unique"] = unique
            if flavor:
                index_d["type"] = flavor

            if dialect_options:
                index_d["dialect_options"] = dialect_options

            indexes.append(index_d)
        indexes.sort(key=lambda d: d["name"] or "~")  # sort None as last
        return indexes if indexes else ReflectionDefaults.indexes()

    @reflection.cache
    def get_unique_constraints(
        self, connection, table_name, schema=None, **kw
    ):
        parsed_state = self._parsed_state_or_create(
            connection, table_name, schema, **kw
        )

        ucs = [
            {
                "name": key["name"],
                "column_names": [col[0] for col in key["columns"]],
                "duplicates_index": key["name"],
            }
            for key in parsed_state.keys
            if key["type"] == "UNIQUE"
        ]
        ucs.sort(key=lambda d: d["name"] or "~")  # sort None as last
        if ucs:
            return ucs
        else:
            return ReflectionDefaults.unique_constraints()

    @reflection.cache
    def get_view_definition(self, connection, view_name, schema=None, **kw):

        charset = self._connection_charset
        full_name = ".".join(
            self.identifier_preparer._quote_free_identifiers(schema, view_name)
        )
        sql = self._show_create_table(
            connection, None, charset, full_name=full_name
        )
        if sql.upper().startswith("CREATE TABLE"):
            # it's a table, not a view
            raise exc.NoSuchTableError(full_name)
        return sql

    def _parsed_state_or_create(
        self, connection, table_name, schema=None, **kw
    ):
        return self._setup_parser(
            connection,
            table_name,
            schema,
            info_cache=kw.get("info_cache", None),
        )

    @util.memoized_property
    def _tabledef_parser(self):
        """return the MySQLTableDefinitionParser, generate if needed.

        The deferred creation ensures that the dialect has
        retrieved server version information first.

        """
        preparer = self.identifier_preparer
        return _reflection.MySQLTableDefinitionParser(self, preparer)

    @reflection.cache
    def _setup_parser(self, connection, table_name, schema=None, **kw):
        charset = self._connection_charset
        parser = self._tabledef_parser
        full_name = ".".join(
            self.identifier_preparer._quote_free_identifiers(
                schema, table_name
            )
        )
        sql = self._show_create_table(
            connection, None, charset, full_name=full_name
        )
        if parser._check_view(sql):
            # Adapt views to something table-like.
            columns = self._describe_table(
                connection, None, charset, full_name=full_name
            )
            sql = parser._describe_to_create(table_name, columns)
        return parser.parse(sql, charset)

    def _fetch_setting(self, connection, setting_name):
        charset = self._connection_charset

        if self.server_version_info and self.server_version_info < (5, 6):
            sql = "SHOW VARIABLES LIKE '%s'" % setting_name
            fetch_col = 1
        else:
            sql = "SELECT @@%s" % setting_name
            fetch_col = 0

        show_var = connection.exec_driver_sql(sql)
        row = self._compat_first(show_var, charset=charset)
        if not row:
            return None
        else:
            return row[fetch_col]

    def _detect_charset(self, connection):
        raise NotImplementedError()

    def _detect_casing(self, connection):
        """Sniff out identifier case sensitivity.

        Cached per-connection. This value can not change without a server
        restart.

        """
        # https://dev.mysql.com/doc/refman/en/identifier-case-sensitivity.html

        setting = self._fetch_setting(connection, "lower_case_table_names")
        if setting is None:
            cs = 0
        else:
            # 4.0.15 returns OFF or ON according to [ticket:489]
            # 3.23 doesn't, 4.0.27 doesn't..
            if setting == "OFF":
                cs = 0
            elif setting == "ON":
                cs = 1
            else:
                cs = int(setting)
        self._casing = cs
        return cs

    def _detect_collations(self, connection):
        """Pull the active COLLATIONS list from the server.

        Cached per-connection.
        """

        collations = {}
        charset = self._connection_charset
        rs = connection.exec_driver_sql("SHOW COLLATION")
        for row in self._compat_fetchall(rs, charset):
            collations[row[0]] = row[1]
        return collations

    def _detect_sql_mode(self, connection):
        setting = self._fetch_setting(connection, "sql_mode")

        if setting is None:
            util.warn(
                "Could not retrieve SQL_MODE; please ensure the "
                "MySQL user has permissions to SHOW VARIABLES"
            )
            self._sql_mode = ""
        else:
            self._sql_mode = setting or ""

    def _detect_ansiquotes(self, connection):
        """Detect and adjust for the ANSI_QUOTES sql mode."""

        mode = self._sql_mode
        if not mode:
            mode = ""
        elif mode.isdigit():
            mode_no = int(mode)
            mode = (mode_no | 4 == mode_no) and "ANSI_QUOTES" or ""

        self._server_ansiquotes = "ANSI_QUOTES" in mode

        # as of MySQL 5.0.1
        self._backslash_escapes = "NO_BACKSLASH_ESCAPES" not in mode

    def _show_create_table(
        self, connection, table, charset=None, full_name=None
    ):
        """Run SHOW CREATE TABLE for a ``Table``."""

        if full_name is None:
            full_name = self.identifier_preparer.format_table(table)
        st = "SHOW CREATE TABLE %s" % full_name

        rp = None
        try:
            rp = connection.execution_options(
                skip_user_error_events=True
            ).exec_driver_sql(st)
        except exc.DBAPIError as e:
            if self._extract_error_code(e.orig) == 1146:
                raise exc.NoSuchTableError(full_name) from e
            else:
                raise
        row = self._compat_first(rp, charset=charset)
        if not row:
            raise exc.NoSuchTableError(full_name)
        return row[1].strip()

    def _describe_table(self, connection, table, charset=None, full_name=None):
        """Run DESCRIBE for a ``Table`` and return processed rows."""

        if full_name is None:
            full_name = self.identifier_preparer.format_table(table)
        st = "DESCRIBE %s" % full_name

        rp, rows = None, None
        try:
            try:
                rp = connection.execution_options(
                    skip_user_error_events=True
                ).exec_driver_sql(st)
            except exc.DBAPIError as e:
                code = self._extract_error_code(e.orig)
                if code == 1146:
                    raise exc.NoSuchTableError(full_name) from e

                elif code == 1356:
                    raise exc.UnreflectableTableError(
                        "Table or view named %s could not be "
                        "reflected: %s" % (full_name, e)
                    ) from e

                else:
                    raise
            rows = self._compat_fetchall(rp, charset=charset)
        finally:
            if rp:
                rp.close()
        return rows


class _DecodingRow:
    """Return unicode-decoded values based on type inspection.

    Smooth over data type issues (esp. with alpha driver versions) and
    normalize strings as Unicode regardless of user-configured driver
    encoding settings.

    """

    # Some MySQL-python versions can return some columns as
    # sets.Set(['value']) (seriously) but thankfully that doesn't
    # seem to come up in DDL queries.

    _encoding_compat = {
        "koi8r": "koi8_r",
        "koi8u": "koi8_u",
        "utf16": "utf-16-be",  # MySQL's uft16 is always bigendian
        "utf8mb4": "utf8",  # real utf8
        "utf8mb3": "utf8",  # real utf8; saw this happen on CI but I cannot
        # reproduce, possibly mariadb10.6 related
        "eucjpms": "ujis",
    }

    def __init__(self, rowproxy, charset):
        self.rowproxy = rowproxy
        self.charset = self._encoding_compat.get(charset, charset)

    def __getitem__(self, index):
        item = self.rowproxy[index]
        if isinstance(item, _array):
            item = item.tostring()

        if self.charset and isinstance(item, bytes):
            return item.decode(self.charset)
        else:
            return item

    def __getattr__(self, attr):
        item = getattr(self.rowproxy, attr)
        if isinstance(item, _array):
            item = item.tostring()
        if self.charset and isinstance(item, bytes):
            return item.decode(self.charset)
        else:
            return item
