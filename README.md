# Geocoder

This program allow you to perform geocoding using Nominatim if you have a raw list of (city, country) data.

## Start geocoding

### 1. Setup database

This script relies on a SQLite database to perform the geocoding.
The database has to be setup beforehand.

```sh
python setup.py
```

```
Database 'db.sqlite3' created successfully.
Query executed successfully.
```

### 2. Setup data with `city` and `country`

`city` and `country` data are stores in the database and the script will append latitude (`lat`) and longitude (`long`) data for each rows.

Use any method to populate the database with `city` and `country` data.

### 3. Run the geocoding

```sh
python main.py --db-path db.sqlite3 --cooldown 60
```

#### CLI Options

|Options|Description|Default|
|--|--|--|
|`-p`, `--db-path`|Path to the database file|`db.sqlite3`|
|`-c`, `--cooldown`|Cooldown between two calls to Nominatim API (in seconds)|`60`|
