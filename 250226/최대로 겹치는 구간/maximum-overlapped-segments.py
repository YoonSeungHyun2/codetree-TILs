n = int(input())  # 구간의 개수
segments = [tuple(map(int, input().split())) for _ in range(n)]  # 구간 입력 받기

cnt = 0
arr = [0] * 201  # OFFSET을 위한 배열 크기 (구간의 범위가 -100 ~ 100이라서)

# 각 구간 처리
for x1, x2 in segments:
    for i in range(x1, x2):
        arr[i + 100] += 1  # OFFSET을 추가하여 배열 인덱스를 다룸
        cnt = max(cnt, arr[i + 100])  # 최댓값 계산

# 결과 출력
print(cnt)
