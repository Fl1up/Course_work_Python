import json
import random

def load_json():
    with open("operations.json","r") as file:
        operations_json = json.load(file)
        random.shuffle(operations_json)
        for i in operations_json:
            return i#operations_json