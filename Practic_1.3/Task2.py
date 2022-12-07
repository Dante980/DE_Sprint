x = "taco cat".replace(" ", "")
i = 0
j = len(x) - 1
# x = [1, 2, 3]
while True:
    if x[i] != x[j]:
        print(False)
        break
    if i >= j:
        print(True)
        break
    i += 1
    j -= 1