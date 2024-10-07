num = int(input())

sum = 0

for i in range(num):
    n = int(input())
    if n % 2 != 0 and n % 3 == 0:
        sum += n

print(sum)