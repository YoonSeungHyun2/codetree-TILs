a, b = map(int, input().split())

if a % 2 == 0:
    a += 1  # a가 짝수면 1을 더해 홀수로 만듦

for i in range(a, b+1, 2):
    print(i, end = " ")