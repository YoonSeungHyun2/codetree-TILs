a, b = map(int, input().split())

if a >= b:
    for i in range(a, b - 1, -1):
        print(i, end = " ")
elif a <= b:
    for i in range(b, a - 1, -1):
        print(i, end = " ")
# for i in range(a, b, -1):
#     if a > b:
#         print(a, b, -1)
#     elif a < b:
#         print(b, a, -1)