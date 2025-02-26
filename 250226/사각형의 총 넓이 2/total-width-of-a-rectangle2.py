OFFSET = 100

N = int(input())  # 사각형의 개수
map_ = [[0] * 201 for _ in range(201)]  # 2D 배열로 초기화

# 사각형을 색칠하는 함수
def get_area(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            map_[i][j] = 1

# 입력 처리 및 사각형 색칠하기
for _ in range(N):
    # 한 줄에 여러 개의 값이 들어오는 경우, split()을 사용하여 분리
    x1, y1, x2, y2 = map(int, input().split())
    get_area(x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET)

# 색칠된 칸의 개수 세기
answer = 0
for i in range(201):
    for j in range(201):
        if map_[i][j] == 1:
            answer += 1

print(answer)
