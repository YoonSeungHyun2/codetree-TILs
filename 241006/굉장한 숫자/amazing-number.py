n = int(input())

if (n % 3 == 0 and n % 2 != 0) or (n % 5 == 0 and n % 2 == 0):
    print("true")
else:
    print("False")