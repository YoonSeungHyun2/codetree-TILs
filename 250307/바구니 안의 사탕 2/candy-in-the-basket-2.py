# N, K = map(int, input().split())
# candy = []
# pos = []

# for _ in range(N):
#     c, p = map(int, input().split())
#     candy.append(c)
#     pos.append(p)

# # Please write your code here.

# n, k 입력
n, k = map(int, input().split())
# linear
linear = [0] * 401
# candy, pos 입력
for _ in range(n):
    candy, pos = map(int, input().split())
    # linear에 추가
    linear[pos] += candy

# 함수들
# in_range(s, e)
def in_range(s, e):
    # s가 양수이고, e가 400 이하면 통과
    return s > 0 and e <= 400

# calc(j)
def calc(j):
    # curr_candy
    curr_candy = 0

    # 현재 범위 내에서
    for i in range(j-k, j+k+1):
        # curr_candy 구하기
        curr_candy += linear[i]
    
    # 구한 candy 갯수 반환
    return curr_candy

# 설계
# max_candy
max_candy = 0

# 완전 탐색 시작
for i in range(1, 401):
    # 양 끝점이 범위 내에 있으면,
    if in_range(i-k, i+k):
        # max_candy 업데이트
        max_candy = max(max_candy, calc(i))

# 출력
print(max_candy)