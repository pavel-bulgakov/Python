# 12. Создайте программу, которая будет рассчитывать сальдо торгового баланса.
# В случае положительного сальдо (превышение экспорта над импортом) подсчитывать прибыль,
# а в случае отрицательного сальдо (превышение импорта над экспортом) рассчитать потери.
# Числа вводятся пользователем с клавиатуры.
print("Каков экспорт?")
exp = int(input())
print("Каков импорт?")
imp = int(input())
if exp>imp :
    print("Сальдо положительное",exp-imp)
else:
    print("Cальдо отрицательное",imp-exp)