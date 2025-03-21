import sys

input = sys.stdin.readline

x = 0 
y = 0

direct = {"N": 0, "E": 1, "S": 2, "W": 3}

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


n = int(input())
cnt = 0

for _ in range(n):
    di, move = input().rstrip().split(" ")
    move = int(move)

    for m in range(move):
        x = x + dx[direct[di]]
        y = y + dy[direct[di]]
        cnt += 1

        if x == 0 and y == 0:
            print(cnt)
            exit()

print(-1)