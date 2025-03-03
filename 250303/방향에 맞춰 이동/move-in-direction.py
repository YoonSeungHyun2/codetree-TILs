# 0 : 동쪽 // 1: 남쪽 // 2: 서쪽 // 3:북쪽
n = int(input())


x, y = 0, 0

# (1, 0): 동쪽으로 +1 // (0,-1): 남쪽으로 +1 // (-1,0) : 서쪽으로 +1 // (0,1): 북쪽으로 +1
dx, dy = [1,0,-1,0], [0,-1,0,1]


for _ in range(n):
    d, s = tuple(input().split())
    s = int(s)
    if( d=='N'):
        dir_num = 3
    elif d=='S' :
        dir_num = 1
    elif d=='W':
        dir_num = 2
    elif d=='E':
        dir_num = 0
    for i in range(s):
        nx, ny = x+dx[dir_num], y+ dy[dir_num]
        x, y = nx, ny

print(x, y)
