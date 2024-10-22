import json

FILE = "ships_data.json"

def load_data():
    """
    Loads a JSON file
    :return: dict
    """
    with open(FILE, "r") as fileobj:
        return json.load(fileobj)
