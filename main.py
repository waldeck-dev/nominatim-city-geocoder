import argparse
from data import DataManager
from geocoder import Geocoder
from time import sleep


def handle(parser):
    args = parser.parse_args()

    cooldown = args.cooldown
    db_path = args.db_path

    manager = DataManager(db_path)

    rows = manager.execute_query_from_file(
        "queries/select_rows_to_geocode.sql"
    )

    geocoder = Geocoder()

    for (row_id, city, country) in rows:
        lat, lon = geocoder.geocode(city, country)

        manager.execute_query_from_file(
            "queries/update_geocoded_data.sql",
            (lat, lon, row_id)
        )

        sleep(cooldown)


def main():
    parser = argparse.ArgumentParser(description=(
        "A CLI program that geocodes places based on city and country names."
    ))

    # Add the "cooldown" option (expects an integer)
    parser.add_argument(
        "-c", "--cooldown",
        type=int,
        default=60,
        help="Cooldown between two calls to Nominatim API (in seconds)."
    )

    # Add the "db-path" option (expects a string)
    parser.add_argument(
        "-p", "--db-path",
        type=str,
        default=("db.sqlite3"),
        help="Path to the database file"
    )

    handle(parser)


if __name__ == "__main__":
    main()
