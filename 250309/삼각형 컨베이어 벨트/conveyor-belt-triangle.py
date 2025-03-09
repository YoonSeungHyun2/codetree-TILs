# n, t = map(int, input().split())

# l = list(map(int, input().split()))
# r = list(map(int, input().split()))
# d = list(map(int, input().split()))

# # Please write your code here.

# n, t 입력
n, t = map(int, input().split())
# tirangle
tirangle = [
    list(map(int, input().split()))
    for _ in range(3)
]

# 함수들
# simulate()
def simulate():
    
    # temp_1, temp_2, temp_3
    temp_1, temp_2, temp_3 = tirangle[0][-1], tirangle[1][-1], tirangle[2][-1]

    # 옮겨주기
    for i in range(n-1, 0, -1):
        tirangle[0][i] = tirangle[0][i-1]
        tirangle[1][i] = tirangle[1][i-1]
        tirangle[2][i] = tirangle[2][i-1]
    
    # temp 넣어주기
    tirangle[0][0] = temp_3
    tirangle[1][0] = temp_1
    tirangle[2][0] = temp_2

# 설계
for _ in range(t):
    simulate()

# 출력
for i in range(3):
    for j in range(n):
        print(tirangle[i][j], end=' ')
    print()