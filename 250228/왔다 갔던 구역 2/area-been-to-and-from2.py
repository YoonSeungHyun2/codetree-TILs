import sys

# 입력 받기
N = int(input().strip())
arr = [0] * 2001  # 길이 2001의 배열 생성

now = 1000  # 시작점을 1000으로 설정

for _ in range(N):
    x, dir = input().split()
    x = int(x)

    if dir == 'L':
        # 왼쪽 이동 시 색칠 구간: [현재 위치 - 1, 현재 위치 - 이동 크기]
        for i in range(now - 1, now - x - 1, -1):
            arr[i] += 1
        now -= x  # 현재 위치 업데이트
    else:
        # 오른쪽 이동 시 색칠 구간: [현재 위치, 현재 위치 + 이동 크기 - 1]
        for i in range(now, now + x):
            arr[i] += 1
        now += x  # 현재 위치 업데이트

# 2번 이상 지나간 구간 개수 구하기
answer = sum(1 for i in arr if i >= 2)
print(answer)
