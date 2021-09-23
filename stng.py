import command_system

def stng():
    message = ''
    message += 'Место - выберите эту команду для настройки текущего местоположения \n'
    message += 'Цикл - выберите эту команду для настройки автоматической рассылки \n'
    message += 'Сброс - эту функцию можно применить как по отдельности, так и для всех настроек одновременно \n'
    return message, ''

stng_command = command_system.Command()

stng_command.keys = ['Настройки', 'settings']
stng_command.desciption = 'Список настроек'
stng_command.process = stng