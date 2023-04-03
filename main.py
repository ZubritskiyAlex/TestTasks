import requests as requests
import json
from datetime import datetime
from collections import Counter

# Task 1
#Дано положительное целочисленное 2-х байтное число.
# Нужно найти значение, которое будет, если поменять байты местами.


def bytes_swap(number) -> str:
    str(number).encode("utf-8")[::-1].decode("utf-8")
    return str(number).encode("utf-8")[::-1].decode("utf-8")

# Task 2



#Task 3
# Необходимо получить HTML-код страницы www.python.org,
# и посчитать сколько раз какие символы встречается в коде страницы.
# Формат вывода определяете сами.
# Вывод программы разместите в файле readme.md.


def url_parse(url: str) -> str:
    """
    :param url:
    :return:
    """
    resp = requests.get(url).text
    report = json.dumps(Counter(resp))
    json_data = json.loads(report)

    with open("readme.md", "w") as outfile:
        json.dump(json_data, outfile)

    return json_data

url_parse("https://www.python.org/")

# Task 4
# Дан json файл.
# Найдите в нём все поля "updated" и поменяйте значение на текущие дату и время в формате ISO 8601.


def _replace_value(json_object: dict) -> None:
    """
    :param json_object:
    :return:
    """
    for key, value in json_object.items():
        if key == "updated":
            json_object[key] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f%z')


def parse_json(json_filepath: str) -> None:
    with open(json_filepath, "r+") as openfile:
        json_object = json.load(openfile)

        if isinstance(json_object, dict):
            _replace_value(json_object)

        else:
            for elem in json_object:
                _replace_value(elem)

        openfile.close()
        json_object = json.dumps(json_object)
        openfile = open(json_filepath, "w")
        openfile.write(json_object)
