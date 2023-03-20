from Utils import load_json
from Utils import number_card
from Utils import load_dates


def main():
    for count_operations in range(5):
        load_dict = load_json()
        for key, values in load_dict.items():
            if values == "EXECUTED":
                load_to = load_dict["to"]
                q = (f'{load_dates(load_dict)}'
                    f' {load_dict["description"]}\n'
                    f'{number_card(load_dict)} -> Счет {"**" + load_to[20:]}\n'
                    f'{load_dict["operationAmount"]["amount"]} {load_dict["operationAmount"]["currency"]["name"]}\n')
                print(q)


main()
""" сортировка по дате .. убрать ошибку по фор ...сделать тесты...."""
