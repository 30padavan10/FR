# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

from sys import argv
import re


def parse_sh_cdp_neighbors(file_str):
    result = {}
    regex1 = '(\S+)[>#]'
    regex2 = '(\S+) +(\w+ \S+) +\d+ +(?:\w )* +\S+ +(\w+ \S+)'
    sw_match = re.search(regex1, file_str)
    sw = sw_match.group(1)
    result.update({sw:{}})
    neighbors = re.finditer(regex2, file_str)
    for match in neighbors:
        dev_po = {match.group(1):match.group(3)}
        result[sw].update({match.group(2):dev_po})
    return result


if __name__  == '__main__':
    file = argv[1]
    with open(file) as src:
        file_str = src.read()
    print(parse_sh_cdp_neighbors(file_str))

