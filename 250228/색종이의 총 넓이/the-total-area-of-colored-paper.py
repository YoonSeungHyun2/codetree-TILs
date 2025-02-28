n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

OFFSET = 100  # 음수 좌표 보정
grid = [[0] * 201 for _ in range(201)]  # 201x201 크기의 격자 생성

def paint(x, y):
    """ 8x8 크기의 색종이를 붙이는 함수 """
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if grid[i][j] == 0:
                grid[i][j] = 1

# 색종이 붙이기
for i in range(n):
    paint(x[i] + OFFSET, y[i] + OFFSET)

# 색종이가 붙은 영역의 넓이 계산
cnt = sum(1 for i in range(201) for j in range(201) if grid[i][j] != 0)

print(cnt)
