# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

des = argv[1]

with open(des, 'r') as src:
        for line in src:
                i = 0
                if line.startswith('!'):
                        pass
                else:
                        for igno in ignore:
                                if igno in line:
                                        i += 1
                        if i == 0:
                                print(line.rstrip())
