# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('/home/padavan/FR/07_files/CAM_table.txt') as src:
    sortlist = []
    for line in src:
        try:
            listm = line.split()
            if len(listm[1]) == 14:
                sortlist.append('{}  {}  {}'.format(listm[0], listm[1], listm[3]))
        except: 'IndexError'
    sortlist.sort()
    print('\n'.join(sortlist))
