import json
import random
from datetime import datetime


def load_json():
    with open("operations.json","r") as file:
        operations_json = json.load(file)
        random.shuffle(operations_json)
        for i in operations_json:
            return i


def load_dates(load_dict):
    load_dates = (load_dict["date"].split("T")[0])
    return load_dates


def number_card(number: str):
    number_card = number["from"].split()[len(number["from"].split()) - 1]
    card = f'{number["from"].replace(f" {number_card}", "")}'
    number_card = number_card[:-10] + "** **** " + number_card[12:]
    number_card = f"{card} {number_card[:4]} {number_card[4:]}"
    return number_card