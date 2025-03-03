n, m = tuple(map(int, input().split()))\

arr = [
    [0]*m
    for _ in range(n)
]

# 밑, 오, 위, 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x = 0
y = 0
for i in range(1, n*m+1):
    arr[y][x] = i
    if (x+dx[d%4] >= m or y+dy[d%4] >= n) or arr[y+dy[d%4]][x+dx[d%4]] != 0:
        d += 1
    x += dx[d%4]
    y += dy[d%4]

for i in range(n):
    for a in arr[i]:
        print(a, end=' ')
    print()