from datetime import datetime
import time
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


user_symbol = ('\033[47m \033[0m')*2

num_all = {
    '0' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '1' : [
        ' ' + user_symbol*4 + '  '*2, 
        ' ' + '  '*2 + user_symbol*2 + '  '*2,
        ' ' + '  '*2 + user_symbol*2 + '  '*2,
        ' ' + '  '*2 + user_symbol*2 + '  '*2,
        ' ' + '  '*2 + user_symbol*2 + '  '*2,
        ' ' + '  '*2 + user_symbol*2 + '  '*2,
        ' ' + user_symbol*6
        ],
    '2' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + user_symbol*6,
        ' ' + user_symbol*2 + '  '*4,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '3' : [
        ' ' + user_symbol*6, 
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + user_symbol*6,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '4' : [
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2
        ],
    '5' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*4,
        ' ' + user_symbol*6,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '6' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*4,
        ' ' + user_symbol*2 + '  '*4,
        ' ' + user_symbol*6,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '7' : [
        ' ' + user_symbol*6, 
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + '  '*4 + user_symbol*2
        ],
    '8' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    '9' : [
        ' ' + user_symbol*6, 
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6,
        ' ' + '  '*4 + user_symbol*2,
        ' ' + user_symbol*2 + '  '*2 + user_symbol*2,
        ' ' + user_symbol*6
        ],
    'sep' : [
        '  '*6,  
        '  '*6,
        '  '*6,
        '  '*2 + user_symbol*2 + '  '*2,
        '  '*6,
        '  '*6,
        '  '*6
        ]
}

while True:
    current_time = datetime.now().strftime("%H%M%S")
    h1 = current_time[0]
    h2 = current_time[1]
    m1 = current_time[2]
    m2 = current_time[3]
    s1 = current_time[4]
    s2 = current_time[5]
    
    for i in range(0, 7, 1):
        clock_str = ''        
        for j in [h1, h2, 'sep', m1, m2, 'sep', s1, s2]:        
            clock_str = clock_str + num_all[j][i]
        print(clock_str.replace('\033[47m \033[0m', f'\033[{41 + int(s2) // 2}m \033[0m'))    

    time.sleep(0.2)   
    clear_screen()