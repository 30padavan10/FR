# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''

from sys import argv
import re


file = argv[1]

regex = '(\S+) +(\S+) +\w+ \w+ +(up|down|administratively down) +(\w+)'

def parse_sh_ip_int_br(file, reg):
    with open(file) as src:
        result = []
        for match in re.finditer(reg, src.read()):
            result.append(match.groups())
        return result



if __name__ == '__main__':
    print(parse_sh_ip_int_br(file, regex))
