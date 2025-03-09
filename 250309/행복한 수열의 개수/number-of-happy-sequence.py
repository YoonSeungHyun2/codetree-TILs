# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.

# n, m 입력
n, m = map(int, input().split())
# grid
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 함수들
# is_happy_row(idx)
def is_happy_row(idx):
    
    # curr_cnt
    curr_cnt = 1
    
    for i in range(n - 1):

        # 다음 숫자와 같으면
        if grid[idx][i] == grid[idx][i+1]:
            # curr_cnt 올려주기
            curr_cnt += 1
        
        # curr_cnt가 m이 되었으면
        if curr_cnt == m:
            # 성공
            return True

        # 다음 숫자와 다르면
        elif grid[idx][i] != grid[idx][i+1]:
            # curr_cnt 초기화
            curr_cnt = 1    
    
    # 다 돌았는데 성공한적 없으면 False
    return False

# is_happy_col(idx)
def is_happy_col(idx):
    
    # curr_cnt
    curr_cnt = 1
    
    for i in range(n - 1):

        # 다음 숫자와 같으면
        if grid[i][idx] == grid[i+1][idx]:
            # curr_cnt 올려주기
            curr_cnt += 1
        
        # curr_cnt가 m이 되면
        if curr_cnt == m:
            # 성공
            return True
        
        # 다음 숫자와 다르면
        elif grid[i][idx] != grid[i+1][idx]:
            # curr_cnt 초기화
            curr_cnt = 1
    
    # 다 돌았는데 성공한적 없으면 False
    return False

# 설계

# 1 * 1 격자인 경우
if n == 1 and m == 1:
    print(2)

# 이외의 경우
else:
    # cnt
    cnt = 0

    # 완전 탐색 시작
    for i in range(n):
        # 가로로 행복하면
        if is_happy_row(i):
            # cnt 올려주기
            cnt += 1
        # 세로로 행복하면
        if is_happy_col(i):
            # cnt 올려주기
            cnt += 1

    # 출력
    print(cnt)