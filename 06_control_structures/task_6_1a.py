# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
IP = input('Enter IP ')
try:
	A,B,C,D = IP.split('.')
	if 256 - int(A) > 0 and 256 - int(B) > 0 and 256 - int(C) > 0 and 256 - int(D) > 0:
		if int(A) > 0 and int(A) <= 223:
        		print('unicast')
		elif int(A) >= 224 and int(A) <= 239:
        		print('multicast')
		elif IP == '255.255.255.255':
        		print('local broadcast')
		elif IP == '0.0.0.0':
        		print('inassigned')
		else:
        		print('unused')
	else:
		print('Incorrect')
except ValueError:
	print('Incorrect IP')
