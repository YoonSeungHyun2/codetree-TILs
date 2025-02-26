# 입력 받기
N, K = map(int, input().split())

# 블록 배열 (0으로 초기화)
block = [0] * (N + 1)
answer = 0

# K개의 구간 입력 처리
for _ in range(K):
    a, b = map(int, input().split())

    # 해당 구간을 1씩 증가
    for i in range(a, b + 1):
        block[i] += 1
        answer = max(answer, block[i])  # 최댓값 업데이트

# 결과 출력
print(answer)
