human_height = int(input("Введите ваш рост в см. : "))
human_weight = int(input("Введите ваш вес в кг. : "))
human_sex = input("Введите ваш пол (м / ж) : ")
human_age = int(input("Введите ваш возраст : "))

human_bmi = round((human_weight / ((human_height/100)**2)), 2)

print(f'Ваш индекс массы тела : {human_bmi}')

print('16' + '='*(int(round(human_bmi, 0))-16) + '|' + '='*(40-int(round(human_bmi, 0))) + '40')

if human_age > 18 and human_age <= 24:
    if human_sex == 'м':
        if human_bmi < 20:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 25:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 19:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 24:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
elif human_age > 24 and human_age <= 34:
    if human_sex == 'м':
        if human_bmi < 21:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 26:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 20:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 25:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')    
elif human_age > 34 and human_age <= 44:
    if human_sex == 'м':
        if human_bmi < 22:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 27:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 21:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 26:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
elif human_age > 44 and human_age <= 54:
    if human_sex == 'м':
        if human_bmi < 23:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 28:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 22:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 27:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
elif human_age > 54 and human_age <= 64:
    if human_sex == 'м':
        if human_bmi < 24:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 29:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 23:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 28:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
elif human_age > 64:
    if human_sex == 'м':
        if human_bmi < 25:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 30:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
    elif human_sex == 'ж':
        if human_bmi < 24:
            print('у вас недостаточный вес - кушайте больше')
        elif human_bmi < 29:
            print('у вас нормальный вес - так держать')
        else:
            print('у вас избыточный вес - кушайте меньше')
