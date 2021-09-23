import command_system
from testweat import ct_tmp

def info():
   message = 'Температура: ' + ct_tmp
   return message, ''

weath_command = command_system.Command()

weath_command.keys = ['погода', 'weather']
weath_command.desciption = 'Погоды нету'
weath_command.process = info