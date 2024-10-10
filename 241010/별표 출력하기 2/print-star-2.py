def solution():
    for i in range(n + 1):
        for j in range(n - i):
            print("*", end = " ")
        print()

n = int(input())
solution()