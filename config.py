import json


def read_token():
    with open("config.json", "r") as file:
        config = json.load(file)

    TOKEN = config.get("TOKEN")

    if not TOKEN:
        raise ValueError("token is not set in config.json")
    return TOKEN


def read_api():
    with open("config.json", "r") as file:
        config = json.load(file)

    POKEMON = config.get("POKEMON_API")

    if not POKEMON:
        raise ValueError("token is not set in config.json")
    return POKEMON
