a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

sum = 0

for i in range(start, end+1):
    if i % 6 == 0 and i % 8 != 0:
        sum += i
print(sum)