a, b, c = map(int, input().split())

min_value = min(a, b, c)
print(1 if a == min_value else 0, 1 if a == b == c else 0)