from datetime import datetime
import time
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

x = 0
sep = [['  '*3, # 
        '  ' + '\u2B1B' + '  ',
        '  ' + '\u2B1B' + '  ',
        '  '*3,
        '  ' + '\u2B1B' + '  ',
        '  ' + '\u2B1B' + '  ',
        '  '*3],
        ['  '*3, # 
        '  '*3,
        '  '*3,
        '  '*3,
        '  '*3,
        '  '*3,
        '  '*3]]

num_all =[['\u2B1B'*6, # 0
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*4 + '  '*2, # 1
        '  '*2 + '\u2B1B'*2 + '  '*2,
        '  '*2 + '\u2B1B'*2 + '  '*2,
        '  '*2 + '\u2B1B'*2 + '  '*2,
        '  '*2 + '\u2B1B'*2 + '  '*2,
        '  '*2 + '\u2B1B'*2 + '  '*2,
        '\u2B1B'*6],
        ['\u2B1B'*6, # 2
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '\u2B1B'*6,
        '\u2B1B'*2 + '  '*4,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*6, # 3
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '\u2B1B'*6,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*2 + '  '*2 + '\u2B1B'*2, # 4
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2],
        ['\u2B1B'*6, # 5
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*4,
        '\u2B1B'*6,
        '  '*4 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*6, # 6
        '\u2B1B'*2 + '  '*4,
        '\u2B1B'*2 + '  '*4,
        '\u2B1B'*6,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*6, # 7
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2,
        '  '*4 + '\u2B1B'*2],
        ['\u2B1B'*6, # 8
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6],
        ['\u2B1B'*6, # 9
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6,
        '  '*4 + '\u2B1B'*2,
        '\u2B1B'*2 + '  '*2 + '\u2B1B'*2,
        '\u2B1B'*6]]



while True:
    current_time = datetime.now().time()
    h1 = current_time.hour // 10
    h2 = current_time.hour % 10
    m1 = current_time.minute // 10
    m2 = current_time.minute % 10
    s1 = current_time.second // 10
    s2 = current_time.second % 10
    x = int(not x)

    print(num_all[h1][0] + '  ' + num_all[h2][0] + sep[x][0] + num_all[m1][0] + '  ' + num_all[m2][0] + sep[x][0] + num_all[s1][0] + '  ' + num_all[s2][0])
    print(num_all[h1][1] + '  ' + num_all[h2][1] + sep[x][1] + num_all[m1][1] + '  ' + num_all[m2][1] + sep[x][1] + num_all[s1][1] + '  ' + num_all[s2][1])
    print(num_all[h1][2] + '  ' + num_all[h2][2] + sep[x][2] + num_all[m1][2] + '  ' + num_all[m2][2] + sep[x][2] + num_all[s1][2] + '  ' + num_all[s2][2])
    print(num_all[h1][3] + '  ' + num_all[h2][3] + sep[x][3] + num_all[m1][3] + '  ' + num_all[m2][3] + sep[x][3] + num_all[s1][3] + '  ' + num_all[s2][3])
    print(num_all[h1][4] + '  ' + num_all[h2][4] + sep[x][4] + num_all[m1][4] + '  ' + num_all[m2][4] + sep[x][4] + num_all[s1][4] + '  ' + num_all[s2][4])
    print(num_all[h1][5] + '  ' + num_all[h2][5] + sep[x][5] + num_all[m1][5] + '  ' + num_all[m2][5] + sep[x][5] + num_all[s1][5] + '  ' + num_all[s2][5])
    print(num_all[h1][6] + '  ' + num_all[h2][6] + sep[x][6] + num_all[m1][6] + '  ' + num_all[m2][6] + sep[x][6] + num_all[s1][6] + '  ' + num_all[s2][6])

    time.sleep(0.5)
    
    clear_screen()
