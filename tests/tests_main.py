import pytest

from Utils import load_json
from Utils import load_dates
from Utils import number_card
def test_read_text():
    assert len(load_dates(load_json("operations.json"))) == 10

def test_load_json():
    with pytest.raises(FileNotFoundError):
        load_json("random")
    assert isinstance(load_json("operations.json"),dict)

def test_key():
    a = load_json("operations.json")
    for key in ["id","state","date","operationAmount","description","from","to"]:
        assert key in a

def test_number_card():
    a = {
    "id": 214024827,
    "state": "EXECUTED",
    "date": "2018-12-20T16:43:26.929246",
    "operationAmount": {
      "amount": "70946.18",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 10848359769870775355",
    "to": "Счет 21969751544412966366"
  }
    assert number_card(a) == "Счет 1084 835976** **** 70775355"
    with pytest.raises(AttributeError):
        number_card({1:1})

def test_date():
    a = {
    "id": 558167602,
    "state": "EXECUTED",
    "date": "2019-04-12T17:27:27.896421",
    "operationAmount": {
      "amount": "43861.89",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73654108430135874305",
    "to": "Счет 89685546118890842412"
  }
    assert load_dates(a) == "12.04.2019"
    with pytest.raises(KeyError):
        load_dates({1:1})


