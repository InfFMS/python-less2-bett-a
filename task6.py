# Натуральное число называется числом Армстронга,
# если сумма цифр числа, возведенных в N-ную степень (где N – количество цифр в числе) равна самому числу.
# Например, 153 = 13 + 53 + 33.
# Найдите все трёхзначные числа Армстронга.


t = []
for i in range(100, 1000):
    q1 = i // 100
    q2 = i // 10 % 10
    q3 = i % 10
    if i == q1 ** 3 + q2 ** 3 + q3 ** 3:
        t.append(i)

print(*t)