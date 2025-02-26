OFFSET = 1000
rect = [[0] * 2001 for _ in range(2001)]  # 2001x2001 배열 초기화

# 직사각형을 그리는 함수
def paint(num, x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            rect[i][j] = num

# 3개의 직사각형 입력받기
for i in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 첫 두 직사각형은 num을 1, 2로 설정하여 색칠
    if i < 2:
        paint(i + 1, x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET)
    # 마지막 직사각형은 겹치는 부분을 0으로 바꿔주기
    else:
        paint(0, x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET)

# 색칠된 칸의 개수 세기
cnt = 0
for i in range(2000):
    for j in range(2000):
        if rect[i][j] != 0:
            cnt += 1

print(cnt)
