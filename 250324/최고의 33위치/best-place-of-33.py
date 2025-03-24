n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# in_range(x, y)
def in_range(x, y):
    # 격자를 벗어나지 않는 지 반환
    return x + 2 < n and y + 2 < n

# get_coin(x, y)
def get_coin(x, y):
    
    # curr_coin
    curr_coin= 0

    # 현 범위 돌면서
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            # curr_coin 구하기
            curr_coin += grid[i][j]
    
    # 반환
    return curr_coin

# 설계
# max_coin
max_coin = 0

# 완전 탐색 시작 -> 왼쪽 상단 기준
for i in range(n):
    for j in range(n):
        # 범위 내에 있으면,
        if in_range(i, j):
            # max_coin update
            max_coin = max(max_coin, get_coin(i, j))

# 출력
print(max_coin)