# N 입력받기
N = int(input())

# N x N 격자 입력받기
grid = [list(map(int, input().split())) for _ in range(N)]

max_coins = 0  # 최대 동전 수를 저장할 변수

# 3x3 격자의 위치를 정하기 위해 격자를 순회
for i in range(N - 2):  # 행을 탐색할 범위
    for j in range(N - 2):  # 열을 탐색할 범위
        # 현재 3x3 격자 내의 동전 수를 계산
        coin_count = 0
        for x in range(3):  # 3x3 격자의 세로 크기
            for y in range(3):  # 3x3 격자의 가로 크기
                coin_count += grid[i + x][j + y]  # 동전 수 세기
        
        # 최대 동전 수 업데이트
        max_coins = max(max_coins, coin_count)

# 결과 출력
print(max_coins)