import requests
import json


def generate_frequency_dict_and_write_to_file():
    write_dict_to_file(frequency())


def write_dict_to_file(d: dict):
    with open('freq.json', 'w', encoding='UTF-8') as file:
        json.dump(d, file, ensure_ascii=False)


def frequency(txt: str = None) -> dict:
    alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'

    if txt is None:
        response = requests.get('https://skazkisameli.ru/raznoe/item/818-priklyucheniya-toma-sojera-chitat')
        txt = response.text

    arr = [i.lower() for i in txt if i.lower() in alphabet]

    d: dict = {}

    for i in arr:
        d[i] = d.get(i, 0) + 1

    return d


def frequency_analyse(d: dict = None):
    if d is None:
        with open('freq.json', encoding='UTF-8') as file:
            d = json.load(file)

    return [element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)]


if __name__ == '__main__':
    generate_frequency_dict_and_write_to_file()
