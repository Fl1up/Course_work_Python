from Utils import load_json
from Utils import load_dates
from Utils import number_card


def main():
    for count_operations in range(5):
        load_dict = load_json()
        for key, values in load_dict.items():
            if values == "EXECUTED":
                load_to = load_dict["to"]

                print(f'{load_dates(load_dict)} {load_dict["description"]}\n'
                      f'{number_card(load_dict)} -> Счет {"**" + load_to[20:]}\n'
                      f'{load_dict["operationAmount"]["amount"]} {load_dict["operationAmount"]["currency"]["name"]}\n')


main()
""" Сделать формат даты .. убрать ошибку по фор """