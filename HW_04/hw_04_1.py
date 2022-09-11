user_var_a = int(input("Введите первое значение : "))
user_var_b = int(input("Введите второе значение : "))
user_var_c = int(input("Введите третье значение : "))


# 1. Если нет ни одого нуля - вывести: "Нет нулевых значений!!!"(Без if - использовать лень)
# print(user_var_a and user_var_b and user_var_c and "Нет нулевых значений!!!")

# 2. Вывести первое ненулевое значение. Если введены все нули - вывести "Введены все нули!" (цикл не использовать) без if - использовать лень
# print(user_var_a or user_var_b or user_var_c or "Введены все нули!")


# 3. Если первое значение больше чем сумма второго и третьего вывести a - b - c
# if user_var_a > (user_var_b + user_var_c):
#     print(user_var_a - user_var_b - user_var_c)

# 4. Если первое значение меньше чем сумма второго и третьего вывести b + c - a
# if user_var_a < (user_var_b + user_var_c):
#     print(user_var_b + user_var_c - user_var_a)

# 5. Если первое значение больше 50 и при этом одно из оставшихся значение больше первого вывести "Вася"
# if user_var_a > 50 and (user_var_a < user_var_b or user_var_a < user_var_c):
#     print("Вася")

# 6. Если первое значение больше 5 или оба из оставшихся значений равны 7 вывести "Петя"
# if user_var_a > 5 or (user_var_b == 7 and user_var_c == 7):
#     print("Петя")