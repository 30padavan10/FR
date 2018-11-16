# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

IP_MASK = input('IP/MASK: ')
IP = IP_MASK.split('/')[0]
MASK = IP_MASK.split('/')[1]
octet = IP.split('.')
octe = list(int(i) for i in octet)
print('Network:\n{0:<8} {1:<8} {2:<8} {3:<8}\n{0:<08b} {1:<08b} {2:<08b} {3:<08b}'.format(octe[0],octe[1],octe[2],octe[3]))
print('\nMask:\n/24\n{0:<8} {1:<8} {2:<8} {3:<8}\n{0:<08b} {1:<08b} {2:<08b} {3:<08b}'.format(255,255,255,0))
