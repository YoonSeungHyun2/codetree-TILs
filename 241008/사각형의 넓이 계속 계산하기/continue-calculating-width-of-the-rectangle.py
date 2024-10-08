while True:
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    c = str(data[2])

    area = a * b
    print(area)

    if c == "C":
        break