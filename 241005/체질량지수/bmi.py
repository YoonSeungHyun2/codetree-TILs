h, w = map(int, input().split())

b = w/(h/100)**2


if b >= 25:
    print(int(b), "\nObesity")

else:
    print(int(b))