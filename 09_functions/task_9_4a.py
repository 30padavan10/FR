# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def nest_command(file):
    ''' суть функции в том, что она проходится отдельно по каждой строке по очереди.
В случае команды первого уровня: в итоговый словарь добавляется словарь, в котором эта команда - ключ и 
значение - пустой список (result.update({level1:[]})).
В случае команды второго уровня, она добавляется в список созданный с ключем level1 (result[level1].append(level2)).
В случае команды третьего уровня:
1. проверка в коде идет раньше команды второго уровня, чтобы команда третьего уровня не попадала под условия
второго уровня.
2. В цикле проходимся по списку из команд второго уровня:
2.1 если это первый элемент списка, то для ключа level1 в качестве значения вместо списка создается словарь,
где ключ это команда второго уровня, а значение - пустой список result.update({level1:{i:[]}})
2.2 если это последующие элементы списка, то во вложенный словарь result[level1] добавляются словари, где ключ
это команды второго уровня, а значения - пустые списки.
2.3 если это последний элемент списка, то во вложенный словарь result[level1][i] добавляется в качестве значения команда
третьего уровня.
3. Есть отдельная проверка на то, что команда третьего уровня идет после команды третьего уровня
type(result[level1]) == dict, тогда команда добавляется в уже существующий словарь result[level1][i].
'''
    result = {}
    with open(file) as src:
        for line in src:
            if line.startswith('!') or line.startswith(' !'):
                pass
            elif line == '\n':                  #убираем пустые строки
                pass
            elif check_ignore(line, ignore):  #используем функцию ignore_command
                pass
            elif line.startswith('  ') and type(result[level1]) == list:
                level3 = result[level1]
                for i in level3:
                    if level3[0] == i:
                        result.update({level1:{i:[]}})
                    else:
                        result[level1].update({i:[]})
                        if i == level3[-1]:
                            result[level1][i].append(line.strip())
            elif line.startswith('  ') and type(result[level1]) == dict:
                 result[level1][i].append(line.strip())
            elif line.startswith(' '):
                level2 = line.strip()
                result[level1].append(level2) 
            else:
                level1 = line.strip()
                result.update({level1:[]})
    
    print(result)
    return result


nest_command('config_r1.txt')

#key - строка верх уровеня(ключ)
#result[key] - список(значение)
#result[key][i] - строка второго уровня



