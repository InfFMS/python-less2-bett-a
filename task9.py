a, b = map(int, input().split())
c, d = map(int, input().split())

if (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1):
    print('YES')
else:
    print('NO')