[![image](https://img.shields.io/pypi/v/package_name.svg)](https://pypi.org/project/package_name)

# DBS

## Getting started
Installation:
```
pip install dbs
```

Run with:
```
python3 -m dbs.query
```

## Using
Execute one query:
```
python3 -m dbs.query 'sqlite://:inmemory:' 'sqls/select.sql'
```

Pipe commands together:
```
export DB_HOST='sqlite://:inmemory:'
python3 -m dbs.query $DB_HOST 'sqls/create.sql'
python3 -m dbs.query $DB_HOST 'sqls/select_table_1.sql' | python3 -m dbs.query $DB_HOST 'sqls/select_table_2.sql'
```

# How to contribute

