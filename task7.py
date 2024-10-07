# Простое число – это число, которое делится только само на себя и на 1.
# Ввести натуральное число N и вывести все простые числа в диапазоне от 2 до N.

def check_prostoe(x):
    q = x // 2
    d = [1, x]
    for i in range(2, q + 1):
        if x % i == 0:
            d.append(i)

    if len(d) == 2:
        return True
    else:
        return False

n = int(input())
for j in range(2, n + 1):
    if check_prostoe(j):
        print(j, end=' ')
