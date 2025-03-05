# n, k　입력
n, k = map(int, input().split())

# linear
linear = [
    0 for _ in range(10001)
]

# pos, point 입력
for _ in range(n):
    pos, point = input().split()
    # linear에 정보추가
    linear[int(pos)] = point

# 함수들
# calc(j)
def calc(j):

    # curr_sum
    curr_sum = 0
    
    # 해당 구간의 합 구하기
    for i in range(j, j + k + 1):
        # G이면,
        if linear[i] == 'G':
            # 1점 추가
            curr_sum += 1
        # H이면,
        elif linear[i] == 'H':
            # 2점 추가
            curr_sum += 2

    # 반환
    return curr_sum

# 설계
# 최대 점수 설정
max_point = 0

# 완전 탐색 시작
for i in range(1, 10001 - k):
    # max_point 업데이트
    max_point = max(max_point, calc(i))

# 출력
print(max_point)

# ---------------------------
# n, k = map(int, input().split())
# x = []
# c = []
# for _ in range(n):
#     pos, char = input().split()
#     x.append(int(pos))
#     c.append(char)

# Please write your code here.

 