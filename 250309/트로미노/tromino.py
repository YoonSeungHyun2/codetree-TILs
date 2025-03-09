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

# 함수들
# in_range_case_1(x, y)
def in_range_case_1(x, y):
    # x는 n-1보다 작고,  y는 m-1보다 작으면 통과
    return x < n-1 and y < m-1

# get_case_1(x, y)
def get_case_1(x, y):
    
    # 90도씩 돌린 4 가지 케이스를 전수조사
    # sum_1
    sum_1 = grid[x][y] + grid[x+1][y] + grid[x+1][y+1]
    # sum_2
    sum_2 = grid[x+1][y] + grid[x+1][y+1] + grid[x][y+1]
    # sum_3
    sum_3 = grid[x+1][y+1] + grid[x][y+1] + grid[x][y]
    # sum_4
    sum_4 = grid[x][y+1] + grid[x][y] + grid[x+1][y]

    # 가장 큰 값을 반환
    return max(sum_1, sum_2, sum_3, sum_4)

# in_range_case_2_row(x, y)
def in_range_case_2_row(x, y):
    # y가 m-2보다 작으면 통과
    return y < m-2

# get_case_2_row(x, y)
def get_case_2_row(x, y):
    # 가로로 연속된 3개의 합을 반환
    return grid[x][y] + grid[x][y+1] + grid[x][y+2]

# in_range_case_2_col(x, y)
def in_range_case_2_col(x, y):
    # x가 n-2보다 작으면 통과
    return x < n-2

# get_case_2_col(x, y)
def get_case_2_col(x, y):
    # 세로로 연속된 3개의 합을 반환
    return grid[x][y] + grid[x+1][y] + grid[x+2][y]

# 설계
# max_sum
max_sum = 0

# 완전 탐색 시작
for i in range(n):
    for j in range(m):
        # 첫 번째 경우에서 범위 내에 있으면
        if in_range_case_1(i, j):
            # max_sum update
            max_sum = max(max_sum, get_case_1(i, j))
        # 두 번째 경우 중 가로로 범위 내에 있으면
        if in_range_case_2_row(i, j):
            # max_sum update
            max_sum = max(max_sum, get_case_2_row(i, j))
        # 두 번째 경우 중 세로로 범위 내에 있으면
        if in_range_case_2_col(i, j):
            # max_sum update
            max_sum = max(max_sum, get_case_2_col(i, j))

# 출력
print(max_sum)