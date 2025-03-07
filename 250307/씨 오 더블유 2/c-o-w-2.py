# n 입력
n = int(input())
# cow 입력
cow = input()

# 설계
# cnt
cnt = 0

# 마지막에서 3번째전까지
for i in range(n-2):
    # C를 찾으면
    if cow[i] == 'C':
        # 그 다음부터 2번째 전까지
        for j in range(i+1, n-1):
            # O를 찾으면
            if cow[j] == 'O':
                # 그 다음부터 마지막까지
                for k in range(j+1, n):
                    # W를 찾으면
                    if cow[k] == 'W':
                        # cnt에 추가
                        cnt += 1

# 출력
print(cnt)