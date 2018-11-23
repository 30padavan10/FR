# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


from sys import argv

des = argv[1]

with open(des, 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
        for line in src:
                i = 0
                for igno in ignore:
                        if igno in line:
                                i += 1
                if i == 0:
                        dest.write(line)
