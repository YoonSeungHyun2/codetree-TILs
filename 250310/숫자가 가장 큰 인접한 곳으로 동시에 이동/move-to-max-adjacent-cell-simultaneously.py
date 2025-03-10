# n, m, t = map(int, input().split())

# # Create n x n grid
# a = [list(map(int, input().split())) for _ in range(n)]

# # Get m marble positions
# marbles = [tuple(map(int, input().split())) for _ in range(m)]
# r = [pos[0] for pos in marbles]
# c = [pos[1] for pos in marbles]

# Please write your code here.

# n, m, t 입력
n, m, t = map(int, input().split())
# grid 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# count 
count = [
    [0] * n
    for _ in range(n)
]
for _ in range(m):
    sx, sy = map(int, input().split())
    sx, sy = sx - 1, sy - 1
    count[sx][sy] = 1

# 함수들
# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    
# move_on_next_count(x, y)
def move_on_next_count(x, y):
    # dxs, dys -> 상하좌우 순서
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    # max_num, ax, ay
    max_num, ax, ay = 0, -1, -1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # nx, ny가 범위 내에 있고, max_num보다 크면
        if in_range(nx, ny) and grid[nx][ny] > max_num:
            # max_num, ax, ay 바꿔주기
            max_num, ax, ay = grid[nx][ny], nx, ny
    # next_count 올려주기
    next_count[ax][ay] += 1

# 설계
for _ in range(t):
    
    # next_count
    next_count = [
        [0] * n
        for _ in range(n)
    ]

    # count를 돌며
    for i in range(n):
        for j in range(n):
            # 구슬을 발견하면
            if count[i][j]:
                # next_count에서 움직임
                move_on_next_count(i, j)
    
    # next_count를 돌며
    for i in range(n):
        for j in range(n):
            # 두개 이상의 구슬을 발견하면
            if next_count[i][j] >= 2:
                # 펑
                next_count[i][j] = 0
    
    # next_count를 count에 복사
    for i in range(n):
        for j in range(n):
            count[i][j] = next_count[i][j]

# ans
ans = 0
# 최종 count를 돌며
for i in range(n):
    for j in range(n):
        # ans에 구슬 추가
        ans += count[i][j]
# 출력
print(ans)