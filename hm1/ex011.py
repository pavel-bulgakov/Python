# 11. Создайте программу, которая, в зависимости от выбранного действия (+, -, *, /)
# будет показывать сумму, разницу, произведение или частное двух чисел, заданных пользователем.
# Например:
# "Первое число: 2"
# "Операция: -"
# "Второе число: 3"
# 2 - 3 = -1
while True:
    num = input("Что хотите сделать? (+,-,*,/): ")
    if num == '0':
        break
    if num in ('+', '-', '*', '/'):
        x = int(input("Первое число="))
        y = int(input("Второе число="))
        if num == '+':
            print(x+y)
        elif num == '-':
            print(x-y)
        elif num == '*':
            print(x*y)
        elif num == '/':
            if y != 0:
                print(x/y)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")