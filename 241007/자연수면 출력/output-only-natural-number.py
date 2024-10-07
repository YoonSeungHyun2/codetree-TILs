a, b = map(int, input().split())


if a == abs(a):
    for i in range(b):
        print(a, end= " ")
else:
    print(0)