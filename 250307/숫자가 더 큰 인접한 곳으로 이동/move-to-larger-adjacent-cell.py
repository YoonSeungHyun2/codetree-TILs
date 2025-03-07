# n, r, c = map(int, input().split())
# a = [[0] * (n + 1) for _ in range(n + 1)]

# for i in range(1, n + 1):
#     row = list(map(int, input().split()))
#     for j in range(1, n + 1):
#         a[i][j] = row[j - 1]

# # Please write your code here.

# n, r, c 입력
n, r, c = map(int, input().split())
r -= 1
c -= 1
# grid 입력
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 함수들
# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
    
# get_next_pos(x, y)
def get_next_pos(x, y):
    # 상하좌우 순서 
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        # 범위 내에 있고, 숫자가 더 크면
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            # 반환
            return (nx, ny)
    
    # 다 돌았는데 없으면 실패
    return False

# 설계
# ans_list
ans_list = [grid[r][c]]

while True:
    # 더 갈 곳이 없으면
    if not get_next_pos(r, c):
        for ans in ans_list:
            print(ans, end=' ')
        # 중단
        break
    # 갈 곳이 있으면
    else:
        # new_r, new_c
        new_r, new_c = get_next_pos(r, c)
        # ans_list에 추가
        ans_list.append(grid[new_r][new_c])
        # r, c 바꿔주기
        r, c = new_r, new_c