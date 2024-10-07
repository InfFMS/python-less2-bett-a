a, b = map(int, input().split())
c, d = map(int, input().split())

if abs(a - c) == abs(b - d) and (a != c and b != d):
    print('YES')
else:
    print('NO')