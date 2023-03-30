from Utils import load_json, load_dates, number_card ,file_json
import pytest


def test_load_json():   # Проверяет на наличие ошибки с данными результатом
    with pytest.raises(FileNotFoundError):
        load_json("random")
    assert isinstance(load_json("operations.json"), dict)


def test_key():   # Проверяет на наличие данных в словаре
    a = load_json("operations.json")
    for key in ["id", "state", "date", "operationAmount", "description", "from", "to"]:
        if key == ["id", "state", "date", "operationAmount", "description", "from", "to"]:
            assert key in a



def test_number_card():   # ППроверяет на наличие ошибки с данными результатом и сравниевает и нужным
    a = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }
    assert number_card(a) == "Счет 9042 492357** **** 46435907"
    with pytest.raises(AttributeError):
        number_card({1: 1})


def test_date():  # Проверяет на наличие ошибки с данными результатом и сравниевает и нужным
    a = {
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05T12:04:13.781725",
    "operationAmount": {
      "amount": "21344.35",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 77613226829885488381"
  }
    assert load_dates(a) == "05.11.2019"
    with pytest.raises(KeyError):
        load_dates({1: 1})
