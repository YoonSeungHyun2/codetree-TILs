# N = int(input())
# a1, b1, c1 = map(int, input().split())
# a2, b2, c2 = map(int, input().split())

# # Please write your code here.

# n 입력
n = int(input())
# comb_1 입력
comb_1 = list(map(int, input().split()))
# comb_2 입력
comb_2 = list(map(int, input().split()))

# 함수들
# open_with_comb_1(a, b, c)
def open_with_comb_1(a, b, c):
    # a, b, c와 comb_1[0], comb_1[1], comb_1[2] 각각의 간격이 모두 2 이내이면 통과
    return (abs(comb_1[0] - a) <= 2 or abs(comb_1[0] - a) >= n-2) and \
    (abs(comb_1[1] - b) <= 2 or abs(comb_1[1] - b) >= n-2) and \
    (abs(comb_1[2] - c) <= 2 or abs(comb_1[2] - c) >= n-2)

# open_with_comb_2(a, b, c)
def open_with_comb_2(a, b, c):
    # a, b, c와 comb_2[0], comb_2[1], comb_2[2] 각각의 간격이 모두 2 이내이면 통과
    return (abs(comb_2[0] - a) <= 2 or abs(comb_2[0] - a) >= n-2) and \
    (abs(comb_2[1] - b) <= 2 or abs(comb_2[1] - b) >= n-2) and \
    (abs(comb_2[2] - c) <= 2 or abs(comb_2[2] - c) >= n-2)

# 설계
# cnt
cnt = 0

# 완전 탐색 시작
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # 첫 번째 조합 또는 두 번째 조합으로 열리면,
            if open_with_comb_1(i,j,k) or open_with_comb_2(i,j,k):
                # cnt에 추가
                cnt += 1

# 출력
print(cnt)