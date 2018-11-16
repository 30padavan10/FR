# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
IP = input('Enter IP ')
while True:
	try:
		A,B,C,D = IP.split('.')
		if 256 - int(A) > 0 and 256 - int(B) > 0 and 256 - int(C) > 0 and 256 - int(D) > 0:
			if int(A) > 0 and int(A) <= 223:
				print('unicast')
				break
			elif int(A) >= 224 and int(A) <= 239:
				print('multicast')
				break
			elif IP == '255.255.255.255':
				print('local broadcast')
				break
			elif IP == '0.0.0.0':
				print('inassigned')
				break
			else:
				print('unused')
				break
		else:
			print('Incorrect')
			IP = input('Enter IP ')

	except ValueError:
		print('Incorrect IP')
		IP = input('Enter IP ')
