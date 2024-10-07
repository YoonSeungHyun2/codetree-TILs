a, b = map(int, input().split())

first = min(a, b)
second = max(a, b)

sum = 0

for i in range(first, second+1):
    if i % 5 == 0:
        sum += i

print(sum)