# -*- coding: utf-8 -*-
from generate_frequency_dict import frequency_analyse, frequency
from main import encrypt


def break_notepad(text: str, d: dict = {}) -> str:
    lst = frequency_analyse()
    lst_from_txt = frequency_analyse(frequency(text))

    notepad = generate_notepad_from_two_lists(lst, lst_from_txt)
    notepad = modificate_dict(notepad, d)

    return encrypt(text, notepad)


def generate_notepad_from_two_lists(lst1: list, lst2: list) -> dict:
    return {k: v for v, k in zip(lst1, lst2)}


def modificate_dict(notepad: dict, d: dict):
    for key, value in d.items():
        notepad_reversed = {v: k for k, v in notepad.items()}
        orignal_letter = notepad_reversed[value]
        notepad[orignal_letter] = notepad[key]
        notepad[key] = value

    print(notepad)

    return notepad


txt = input()
print(break_notepad(txt,
                    {'н': 'е', 'ц': 'т', 'ч': 'ь', 'о': 'н', 'п': 'л', 'э': 'з', 'б': 'б', 'м': 'и', 'г': 'в', 'ж': 'ы',
                     'к': 'р', 'ш': 'п', 'и': 'о', 'х': 'ж', 'й': 'а', 'в': 'к', 'д': 'д', 'щ': 'с'}))
"""В тексте длиннее подбирать ключ, если известны несколько слов и их местоположение, то дешифровать проще, меньше перестановок надо"""
