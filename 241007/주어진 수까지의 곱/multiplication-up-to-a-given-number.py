a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

prod = 1

for i in range(start, end+1):
    prod *= i
print(prod)