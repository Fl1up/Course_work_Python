import json

from Utils import load_json, load_dates, number_card
import pytest

@pytest.fixture()
def test_data():
    my_code =r'/home/german/PycharmProjects/course_work/operations.json'
    with open(my_code, "r") as file:
        data = json.load(file)
        return data


def test_load_dates(test_data):
    result = load_dates(test_data)
    with pytest.raises(TypeError):
        assert len(result) == 5

def test_number_card():
    with pytest.raises(AssertionError):
        assert number_card("1234567890123456") == "1234 5678 9012 3456"

def test_load_json(test_data):
    my_code = r'/home/german/PycharmProjects/course_work/operations.json'
    result = load_json(my_code)
    with pytest.raises(TypeError):
        assert len(result) == 5
