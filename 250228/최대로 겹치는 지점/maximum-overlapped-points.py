import sys

# 입력 받기
N = int(input())
arr = [0] * 101  # 길이 101의 배열 생성

# 선분 정보를 입력받아 배열에 반영
for _ in range(N):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2 + 1):  # 구간을 포함하므로 x2까지 반복
        arr[i] += 1

# 최대 선분 개수 찾기
answer = max(arr)
print(answer)
