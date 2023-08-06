DuckDB-Cursor
=============

DuckDB-Cursor is simple [DuckDB](https://www.duckdb.org) wrapper.


Install
-------

First install library,
```
pip install duckdb-cursor
```


Usage
-----

Create an DB object and initialise it with the application,
```python
from duckdb import connect
from duckdb_cursor import CURSOR

cur = CURSOR(connect("db.duckdb"))
cur.set("INSERT INTO users VALUES(1, ?);", ('Wendys', ))
del cur
```

can select one row,
```python
cur = CURSOR(connect("db.duckdb"))
row = cur.get("SELECT name FROM users WHERE id=1;", as_dict=True, one=True)
del cur

print(row['name'])
```

can select all rows,
```python
cur = CURSOR(connect("db.duckdb"))
rows = cur.get("SELECT name FROM users;")
del cur

print(rows)
```


Contributing
------------

DuckDB-Cursor is developed on [GitLab](https://gitlab.com/wcorrales/duckdb-cursor). You are very welcome to
open [issues](https://gitlab.com/wcorrales/duckdb-cursor/issues) or
propose [merge requests](https://gitlab.com/wcorrales/duckdb-cursor/merge_requests).


Help
----

This README is the best place to start, after that try opening an
[issue](https://gitlab.com/wcorrales/duckdb-cursor/issues).
