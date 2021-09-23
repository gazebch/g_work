import command_system

def mest():
   message = 'Введите через запятую город и страну. Например "Курск, Россия"'
   return message, ''

mest_command = command_system.Command()

mest_command.keys = ['место', 'Place']
mest_command.description = 'Указать свое местоположение'
mest_command.process = mest