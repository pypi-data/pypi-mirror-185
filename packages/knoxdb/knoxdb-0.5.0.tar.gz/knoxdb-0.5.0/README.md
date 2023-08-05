# KnoxDB Python Library

[![pypi](https://img.shields.io/pypi/v/knoxdb.svg)](https://pypi.org/project/knoxdb/)

Table of contents
=================

<!--ts-->
   * [Install](#install)
   * [Usage](#usage)
   * [Feedback](#feedback)

<!--te-->


## Install

This library only supports `python3`

```console
$ pip install knoxdb
```


## Usage

```python
import knoxdb
from knoxdb import knox
```

Create a new DB with a custom name. This returns back information about the DB you can store to easily access it again.
```python
new_db = knox.create(db_name="test_db")
```

Get a DB Instance from the ID returned after creating an instance

```python
db = knox.get_from_id(id="test_db_id")
```

Connect to DB Instance

```python
conn = knox.connect(id="test_db_id")
```

Close connection to DB

```python
knox.close_db_connection(conn=conn)
```

Query the DB Instance by passing in a SQL Command

```python
conn = knox.connect(id="test_db_id")
sql_string = "CREATE TABLE \"User\" (id serial PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL)"
db_query = knox.query(conn=conn, sql_string=sql_string, close_conn=True)
```

## Feedback

Feel free to send me feedback or feature requests on my [Website](https://knox.framer.website). Feature requests are always welcome.

If there's anything you'd like to chat about, please feel free to email me at knox.dobbins@gmail.com!


