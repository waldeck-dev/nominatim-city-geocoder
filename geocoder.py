import json
from urllib.request import urlopen
from urllib.parse import quote


class Geocoder:

    BASE_URL = "https://nominatim.openstreetmap.org/search"
    FORMAT = "jsonv2"

    def get_query(self, city, country):
        return (
            f"city={quote(city)}&country={quote(country)}"
            f"&format={self.FORMAT}&limit=1"
        )

    def geocode(self, city, country):
        url = f"{self.BASE_URL}?{self.get_query(city, country)}"

        with urlopen(url) as response:
            raw_res = response.read()

            try:
                res = json.loads(raw_res)[0]
                return float(res["lat"]), float(res["lon"])

            except (KeyError, ValueError, IndexError):
                return -1.0, -1.0
