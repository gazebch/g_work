import command_system

def info():
    message = ''
    message += 'Начать - начало работы \n Настройки - перейти к настройки информирования \n'
    message += 'Место - выбрать текущее местоположение \n Цикл - задать переодичность информирования \n'
    message += 'Сброс - сбросить настройки \n Погода - узнать погоду на текущий момент времени'
    return message, ''

info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.desciption = 'Покажу список команд'
info_command.process = info