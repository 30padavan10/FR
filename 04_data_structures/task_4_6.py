# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#Заменяем все знаки пробелами, берем срез строки без знака О, преобразуем строку в список.
#Выводим строку с форматированием из элементов списка
ospflist = ospf_route.replace(',', ' ').replace('[', ' ').replace(']', ' ')[2:].split()
print('Protocol: {:>30}\nPrefix: {:>32}\nAD/Metric: {:>29}\nNext-hop: {:>30}\nLast update: {:>27}\nOutbound Interface: {:>20}'.format('OSPF', ospflist[0], ospflist[1], ospflist[3], ospflist[4], ospflist[5]))
