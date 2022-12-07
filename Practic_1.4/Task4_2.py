from fileinput import close
from inspect import stack
str_ = input()
stack1 = []
'''
def Function90(i, j, h):
    return i*j*h

e = Function90(1, 2, 3)
'''
# организуем первый стэк
for i in str_:
    stack1.append(i)
# для строки не работает метод append и pop, так что заполняем данные из строки в первый стэк
stack2 = []
# второй стек для перебора
open_ = ["{", "[", "("]
# массив открывающих скобок
verification_ = {"{":"}", "[":"]", "(":")"}
# проверяем для какой скобки какая скобка будет закрывающей
while (True):
    if stack1 == []:
        # вводная строка или пустая или мы закончили её обработку 
        print(True)
        break
    # i1 = [1, 2, 3]
    # e = i1.pop()
    ch1 = stack1.pop()
    # достаем верхнее значени из первого стека
    if ch1 in open_:
        # порверяем есть ли наш конкретный элемент в массиве открытых скобок
        try:
            ch2 = stack2.pop()
            # достаем верний элемент из стека2. Если его нет, перехватываем ошибку блоком try-except. В except говорим,
            # что получили открытую скобку без пары
            if verification_[ch1] != ch2:
                # проверяем, одного ли типа скобки с ch1 и ch2
                print(False)
                break
        except:
            print(False)
            break
    else:
        # получили закрытую скобку, следовательно добавляем её в стэк2
        stack2.append(ch1)
        # it =[1, 2, 3]
        # it.append(4)