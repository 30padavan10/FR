# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''
import re
import glob
import yaml
import sqlite3
import os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
sw_filename = 'switches.yml'


def parse_dhcp(dhcp_snoop_files):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []

    for file in dhcp_snoop_files:
        with open(file) as src:
            matches = re.finditer(regex, src.read())
            for match in matches:
                match_str = list(match.groups())
                match_str.append(file[:file.index('_dhcp')])
                result.append(match_str)
    return result

def parse_switches(sw_filename):
    with open(sw_filename) as src:
        switches = yaml.load(src)
    return switches



def insert_to_db(result, switches, db_filename):
    exists = os.path.exists('dhcp_snooping.db')
    if exists:
        conn = sqlite3.connect(db_filename)
        for row in result:
            try:
                query = 'insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'
                with conn:
                    conn.execute(query, row)
                    print('Success {}'.format(row))
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)


        for items in switches['switches'].items():
            try:
                query = 'insert into switches (hostname, location) values (?, ?)'
                with conn:
                    conn.execute(query, items)
                    print('Success {}'.format(items))
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)
        conn.close()
    else:
        print('Need create db')


if __name__ == '__main__':
    insert_to_db(parse_dhcp(dhcp_snoop_files), parse_switches(sw_filename), db_filename)
