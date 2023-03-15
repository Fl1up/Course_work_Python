from Utils import load_json
def main():
    for count_operations in range(5):
        load_dict = load_json()
        for key, values in load_dict.items():
            if values == "EXECUTED":
                load_one_dict = load_dict["operationAmount"]
                load_two_dict = load_one_dict["currency"]

                print(f'{load_dict["date"]} {load_dict["description"]}\n'
                      f'{load_dict["from"]} {load_dict["to"]}\n' 
                      f'{load_one_dict["amount"]} {load_two_dict["name"]}\n')


main()