print('Инструкция :\nробот понимает следующие команды\n'
      'шаг вверх - u\n'
      'шаг вниз - d\n'
      'шаг вправо - r\n'
      'шаг влево - l\n'
      'пробел - окончание движение робота\n'
      'количество шагов в выбранном направлении вводится через пробел\n'
      'пример: "u 5" - робот пройдет вверх на 5 шагов\n')

robot_x = 0
robot_y = 0
robot_path = 0
robot_history = []

while True:

    robot_command = input('введите команду : ')
    robot_command_list = robot_command.split(' ')
    
    if robot_command == ' ':
        print('движение робота окончено')
        break
    elif len(robot_command_list) < 2 or len(robot_command_list) > 2:
        print('команда введена некорректно')
    else:
        match robot_command_list[0]:
            case 'u':
                robot_x = robot_x + int(robot_command_list[1])
                robot_path = robot_path + int(robot_command_list[1])
                robot_history.append(''.join(robot_command_list))        
            case 'd':
                robot_x = robot_x - int(robot_command_list[1])
                robot_path = robot_path + int(robot_command_list[1])
                robot_history.append(''.join(robot_command_list))        
            case 'r':
                robot_y = robot_y + int(robot_command_list[1])
                robot_path = robot_path + int(robot_command_list[1])
                robot_history.append(''.join(robot_command_list))        
            case 'l':
                robot_y = robot_y - int(robot_command_list[1])
                robot_path = robot_path + int(robot_command_list[1])
                robot_history.append(''.join(robot_command_list))        
            case _:
                print('команда введена некорректно')

print(f'\nробот находится в точке с координатами ( {robot_x} , {robot_y} )')
print(f'робот прошел шагов -  {robot_path}')
print(f'история пути робота {" - ".join(robot_history)}')
print(f'растояние от робота до начала пути - {round(((robot_x)**2 + (robot_y)**2)**0.5, 2)}')