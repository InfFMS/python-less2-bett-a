'''
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

if a1 == a2 and b1 == b2:
    print(a1, b1)

#elif a2 <= a1 and b2 <= b1 and a1 < b2:
   # print(a1, b2)

elif b1 == a2 and a1 < b2:
    print(b1)

#elif a1 <= a2 and b1 <= b2 and a2 < b2:
   # print(a2, b1)

elif a2 < b1 and a1 == b2:
    print(a1)

elif (a1 < a2 and b1 < a2 and b1 < a2) or (a2 < a1 and b2 < a1 and b2 < a1):
    print('пустое множество')
'''

# Ну, я не доделала :')