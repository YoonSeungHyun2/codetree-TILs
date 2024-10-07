n = int(input())

for i in range(n, 101):
    if 100 >= i >= 90:
        print("A", end = " ")
    elif 90 > i >= 80:
        print("B", end = " ")
    elif 80 > i >= 70:
        print("C", end = " ")
    elif 70 > i >= 60:
        print("D", end = " ")
    else:
        print("F", end = " ")