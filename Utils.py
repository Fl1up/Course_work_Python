import datetime, operator, re
from datetime import datetime


file_json = 'operations.json'
status = 'EXECUTED'


def load_dates(load_dict):
    """
    Создает цикл,сплитит его фильтрует по дате и выводит его.
    """
    count = 0
    for i in load_dict:
        if count == 5:
            return
        if len(i) > 0 and i['state'] == status:

            split_date = i['date'].split('T')[0]
            datetime_object = datetime.strptime(split_date, '%Y-%m-%d').date().strftime('%d.%m.%Y')
            cost = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
            print(f'{datetime_object} {i["description"]}')
            s1 = re.sub("[^A-Za-z0-9]", "", number_card(i["to"][21:]))
            if 'открытие' in i['description'].lower():
                print(f'{number_card(i["to"])}')
            else:
                print(f'{number_card(i["from"])} -> {"**" + s1}')
            print(cost)
            print()
            count += 1


def number_card(number: str):
    """
    Редактирует формат номера карты и счета в том форме которая нужно
    """
    payment_type = f'{number.split()[len(number.split()) - 1]}'
    card_type = f'{number.replace(f" {payment_type}", "")}'
    payment_type = payment_type[:-10] + '** **** ' + payment_type[12:]
    payment_type = f'{card_type} {payment_type[:4]} {payment_type[4:]}'
    return payment_type


def load_json(file_json):
    """
    Функция открывает файл сортирует по дате и выводит
    """
    with open(file_json, 'r', encoding='UTF-8') as file:
        sorting_running = list(eval(file.read()))  # анализ вырадения и запуск его
    sortint_date = [date for date in sorting_running if 'date' in date]
    sortint_date.sort(key=operator.itemgetter('date'), reverse=True)
    return load_dates(sortint_date)
