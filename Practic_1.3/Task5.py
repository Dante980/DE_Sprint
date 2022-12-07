x1 = input()
x2 = input()

value1 = 0
value2 = 0
# в value1 и value2 будем хранить числа в десятичной системе. Инициализируем их
for i in range(len(x1)):
    # получаем первое число в десятичной системе
    value1 += pow(2, i) * int(x1[i])
for i in range(len(x2)):
    # получаем второе число в десятичной системе
    value2 += pow(2, i) * int(x2[i])
result_ = value1 * value2
result_ = bin(result_)[2:]
print(result_)