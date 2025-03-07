# n, t = map(int, input().split())
# u = list(map(int, input().split()))
# d = list(map(int, input().split()))

# # Please write your code here.
# n, t 입력
n, t = map(int, input().split())
# conbeyor_belt 입력
conbeyor_belt = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 함수들
# simulate()
def simulate():
    
    # temp_up, temp_down
    temp_up, temp_down = conbeyor_belt[0][-1], conbeyor_belt[1][-1]
    
    # 옮겨주기
    for i in range(n-1, 0, -1):
        # 윗 줄
        conbeyor_belt[0][i] = conbeyor_belt[0][i-1]
        # 아랫 줄
        conbeyor_belt[1][i] = conbeyor_belt[1][i-1]
    
    # temp_up, temp_down 넣어주기
    conbeyor_belt[0][0], conbeyor_belt[1][0] = temp_down, temp_up

# 설계
for i in range(t):
    # simulate
    simulate()

# 출력
for i in range(2):
    for j in range(n):
        print(conbeyor_belt[i][j], end=' ')
    print()