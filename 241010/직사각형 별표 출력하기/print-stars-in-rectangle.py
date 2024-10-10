def solution ():
    for i in range(n):
        for j in range(m):
            print("*", end = " ")
        print()

n, m = map(int, input().split())
solution()