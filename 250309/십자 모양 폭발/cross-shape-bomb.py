# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]
# r, c = map(int, input().split())

# # Please write your code here.
# n 입력
n = int(input())
# grid 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# bomb_x, bomb_y
bomb_x, bomb_y = map(int, input().split())
bomb_x -= 1
bomb_y -= 1

# 함수들
# make_drop(curr_col)
def make_drop(curr_col):

    # temp_col
    temp_col = []

    for r in range(n-1, -1, -1):
        # 숫자가 있으면,
        if grid[r][curr_col]:
            temp_col.append(grid[r][curr_col])
    
    # shortage
    shortage = n - len(temp_col)

    # 부족분 0으로 채워주기
    for _ in range(shortage):
        temp_col.append(0)
    
    for i in range(n-1, -1, -1):
        grid[i][curr_col] = temp_col[(n-1) - i]

# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# bomb()
def bomb():
    # bomb_pow
    bomb_pow = grid[bomb_x][bomb_y]
    
    # 원심지 터뜨려주기
    grid[bomb_x][bomb_y] = 0

    # dxs, dys
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(1, bomb_pow):
        for dx, dy in zip(dxs, dys):
            nx, ny = bomb_x + dx * i, bomb_y + dy * i
            # 범위 내에 있다면
            if in_range(nx, ny):
                # 터뜨려주기
                grid[nx][ny] = 0

# 설계
# bomb
bomb()

# 한열씩 내려주기
for i in range(n):
    make_drop(i)

# 출력
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()