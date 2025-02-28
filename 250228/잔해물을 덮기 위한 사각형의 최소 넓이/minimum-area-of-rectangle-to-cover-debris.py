OFFSET = 1000
MAX_R = 2000
N = 2

# 좌표 배열 초기화
x1, y1, x2, y2 = [0] * N, [0] * N, [0] * N, [0] * N

# 입력 받기
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# OFFSET 적용
for i in range(N):
    x1[i] += OFFSET
    y1[i] += OFFSET
    x2[i] += OFFSET
    y2[i] += OFFSET

# 직사각형 표시할 2D 배열
checked = [[0] * (MAX_R + 1) for _ in range(MAX_R + 1)]

# 직사각형 영역 표시
for i in range(N):
    for x in range(x1[i], x2[i]):
        for y in range(y1[i], y2[i]):
            checked[x][y] = i + 1

# 첫 번째 직사각형 잔해물 여부 및 최소/최대 좌표 구하기
min_x, max_x = MAX_R, 0
min_y, max_y = MAX_R, 0
first_rect_exist = False

for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# 넓이 계산
area = (max_x - min_x + 1) * (max_y - min_y + 1) if first_rect_exist else 0

print(area)
