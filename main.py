from Utils import load_json, number_card, load_dates

def main():
    operations = []
    for _ in range(5):
        operations.append(load_json("operations.json"))

    for operation in operations:
        load_dict = load_json("operations.json")

        for keys, values in load_dict.items():
            if values == "EXECUTED":
                load_to = load_dict["to"]

                print(f'{load_dates(operation)} {load_dict["description"]}\n'
                    f'{number_card(load_dict)} -> Счет {"**" + load_to[20:]}\n'
                    f'{load_dict["operationAmount"]["amount"]} {load_dict["operationAmount"]["currency"]["name"]}\n')


main()
