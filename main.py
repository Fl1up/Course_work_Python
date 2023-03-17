from Utils import load_json
def main():
    for count_operations in range(5):
        load_dict = load_json()
        for key, values in load_dict.items():
            if values == "EXECUTED":
                load_to = load_dict["to"]
                load_dates = (load_dict["date"].split("T")[0])

                number_card = f'{load_dict["from"].split()[len(load_dict["from"].split()) - 1]}'
                number_card = number_card[:-10] + '** **** ' + number_card[12:]
                number_card = f'{number_card[:4]} {number_card[4:]}'

                print(f'{load_dates} {load_dict["description"]}\n'
                      f'{number_card} -> Счет {"**" + load_to[20:]}\n'
                      f'{load_dict["operationAmount"]["amount"]} {load_dict["operationAmount"]["currency"]["name"]}\n')

main()