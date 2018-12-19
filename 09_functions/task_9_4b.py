from pprint import pprint

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
    ''' Все как в 9.4 только добавлены условия для глубины "   ". Сделано условие на случай,
если появляется после строки "   " появляет строка с "  ", но не сделано условие для случая когда
вновь появляется " ".
'''
    result = {}
    with open(file) as src:
        for line in src:
            if line.startswith('!') or line.startswith(' !') or line.startswith('  !'):
                pass
            elif line == '\n':                  #убираем пустые строки
                pass
            elif check_ignore(line, ignore):  #используем функцию ignore_command
                pass

            elif line.startswith('   ') and type(result[level1][sp3[-1]]) == list:
                sp4 = result[level1][sp3[-1]]
                for level3 in sp4:
                    if sp4[0] == level3:
                        result[level1].update({sp3[-1]:{level3:[]}})
                    else:
                        result[level1][sp3[-1]].update({level3:[]})
                        if level3 == sp4[-1]:
                             result[level1][sp3[-1]][level3].append(line.strip())

            elif line.startswith('   ') and type(result[level1][sp3[-1]]) == dict:
                result[level1][sp3[-1]][sp4[-1]].append(line.strip())

            elif line.startswith('  ') and type(result[level1]) == list:
                sp3 = result[level1]
                for level2 in sp3:
                    if sp3[0] == level2:
                        result.update({level1:{level2:[]}})
                    else:
                        result[level1].update({level2:[]})
                        if level2 == sp3[-1]:
                            result[level1][level2].append(line.strip())
                
            elif line.startswith('  ') and type(result[level1]) == dict and type(result[level1][sp3[-1]]) == list:
                result[level1][sp3[-1]].append(line.strip())

            elif line.startswith('  ') and type(result[level1][sp3[-1]]) == dict:
                sp4.append(line.strip())
                result[level1][sp3[-1]].update({sp4[-1]:[]})

            elif line.startswith(' ') and type(result[level1]) == dict: 
                sp3.append(line.strip())
                result[level1].update({line.strip():[]})

            elif line.startswith(' ') and type(result[level1]) == list:
                result[level1].append(line.strip())

            else:
                level1 = line.strip()
                result.update({level1:[]})

    pprint(result)
    return result


nest_command('config_r2.txt')
