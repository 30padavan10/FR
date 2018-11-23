# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

with open('/home/padavan/FR/07_files/ospf.txt') as f:
	lines = f.read().split('O')
	for line in lines:
		lline = line.strip().replace('[',' ').replace(']',' ').replace(',',' ').split()
		if 'via' in lline:
			A,B,C,D,E,F = lline
			print('\nProtocol: {:<15}\nPrefix: {:<15}\nAD/Metric: {:<15}\nNext-hop: {:<15}\nLast update: {:<15}\nOutbound Int: {:<15}\n'.format('OSPF',A,B,D,E,F))
