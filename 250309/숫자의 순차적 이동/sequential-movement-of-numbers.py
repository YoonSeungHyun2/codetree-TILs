# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# n, m 입력
n, m = map(int, input().split())
# grid 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# change(x, y)
def change(x, y):
    
    # curr_max
    curr_max = 0

    # dxs, dys
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 범위 내에 있고, 최댓값보다 크다면
        if in_range(nx, ny) and grid[nx][ny] > curr_max:
            # cx, cy, curr_max update
            cx, cy, curr_max = nx, ny, grid[nx][ny]

    # temp
    temp = grid[x][y]

    # 바꿔주기
    grid[x][y] = grid[cx][cy]
    grid[cx][cy] = temp

# simulate(curr_num)
def simulate(curr_num):
    
    # grid를 돌면서
    for i in range(n):
        for j in range(n):
            # curr_num을 찾으면
            if grid[i][j] == curr_num:
                # 바꿔주고
                change(i, j)
                # 함수종료
                return

# 설계
# 총 m번 반복
for _ in range(m):

    # 현재 움직여줄 번호
    for i in range(1, n**2 + 1):
        # simulate(i)
        simulate(i)

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()