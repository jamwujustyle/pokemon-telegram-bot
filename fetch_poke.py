import requests
from typing import Final


def fetch_pokemon(api, name):
    url = f"{api}{name.lower()}"
    print(f"fetching from {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as ex:
        return {"error ": f"failed to fetch pokemon data: {ex}"}
