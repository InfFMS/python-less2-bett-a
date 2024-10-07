a, b = map(int, input().split())
c, d = map(int, input().split())

if (abs(a - c) == abs(b - d)) or (a == b and b != d) or (a != c and b == d):
    print('YES')
else:
    print('NO')