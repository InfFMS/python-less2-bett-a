#Найдите все пятизначные числа, которые при делении на 133 дают в остатке 125, а при делении на 134 дают в остатке 111

l = []
for i in range(10000, 100000):
    if (i % 133 == 125) and (i % 134 == 111):
        l.append(i)

print(*l)