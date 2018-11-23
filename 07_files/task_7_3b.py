# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input('Enter vlan: ')

with open('/home/padavan/FR/07_files/CAM_table.txt') as src:
    sortlist = []
    for line in src:
        try:
            listm = line.split()
            if len(listm[1]) == 14 and vlan == listm[0]:
                sortlist.append('{}  {}  {}'.format(listm[0], listm[1], listm[3]))
        except: 'IndexError'
    sortlist.sort()
    print('\n'.join(sortlist))
