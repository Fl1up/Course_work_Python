import json, random, datetime
from datetime import datetime


def load_json(fileatsh):
    """
    функция открывает json и рандомит 1 слово возвращая его
    """
    with open(fileatsh,"r") as file:
        operations_json = json.load(file)
        random.shuffle(operations_json)
        for random_json in operations_json:
            return random_json


def load_dates(load_dict):
    """
    Фильтрует дату оставляя только нужное
    """
    load_dates = (load_dict["date"].split("T")[0])
    load_dates_change = datetime.strptime(load_dates, '%Y-%m-%d').date().strftime('%d.%m.%Y')
    return load_dates_change


def number_card(number):
    """
    Редактирует формат номера карты и счета который нам нужен
    """
    number_card = number.get('from').split()[len(number.get('from').split()) - 1]
    card = number.get('from').replace(f" {number_card}", "")
    number_card = number_card[:-10] + "** **** " + number_card[12:]
    number_card = f"{card} {number_card[:4]} {number_card[4:]}"
    return number_card
