import json
import random
import datetime


def load_json():
    with open("operations.json","r") as file:
        operations_json = json.load(file)
        random.shuffle(operations_json)
        for i in operations_json:
            return i


def load_dates(load_dict):
    load_dates = (load_dict["date"].split("T")[0])
    return load_dates

def date_improvement(date):
    a = load_dates(date).split("-")
    b = f"{a[2]}.{a[1]}.{a[0]}"
    return b

def number_card(number):
    number_card = number['from'].split()[len(number['from'].split()) - 1]
    card = number['from'].replace(f" {number_card}", "")
    number_card = number_card[:-10] + "** **** " + number_card[12:]
    number_card = f"{card} {number_card[:4]} {number_card[4:]}"
    return number_card



