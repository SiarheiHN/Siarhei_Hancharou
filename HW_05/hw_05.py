# написать программу которая: запрашивает у пользователя логин
# Есть функция котороя выводит сумму на счете
# Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
# Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен

user_login = input("Enter your login :")

import functools
def login_required(func):
    @functools.wraps(func)
    def wrapper_decorator():
        if user_login == 'admin':
            return func()
        print('Access is denied')
    return wrapper_decorator

@login_required
def account_balance():
    print('Account balance : 1.000.000 $')

account_balance()