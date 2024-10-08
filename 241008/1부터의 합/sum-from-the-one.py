n = int(input())
sum = 0

for i in range(1, 101, 1):
    sum += i
    if sum >= n:
        print(i, end = " ")
        break