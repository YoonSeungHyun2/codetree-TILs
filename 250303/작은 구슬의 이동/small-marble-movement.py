import sys


input = sys.stdin.readline


n, time = map(int, input().split(" "))

x, y, nd = input().rstrip().split(" ")

x = int(x) - 1
y = int(y) - 1

direct = {"U": 0, "R":1, "D": 2, "L":3}
# U <-> D, R <-> L
dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0] 


for t in range(time):
    ny = y + dx[direct[nd]]
    nx = x + dy[direct[nd]]

    if not (0 <= nx and nx < n and  0<= ny and ny <n):
        if nd == 'L': nd = "R"
        elif nd == 'R': nd = "L"
        elif nd == 'U': nd = "D"
        elif nd == 'D': nd = "U"
    else:
        x = nx
        y = ny

print(x+1, y+1)