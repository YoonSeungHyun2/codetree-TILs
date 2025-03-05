# n 입력
n = int(input())

# a, b, c 입력 (비밀번호)
a, b, c = map(int, input().split())

# 함수: 자물쇠가 열리는 조건 체크
def is_open(x, y, z):
    return abs(x - a) <= 2 or abs(y - b) <= 2 or abs(z - c) <= 2

# 가능한 모든 조합 탐색
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if is_open(i, j, k):
                cnt += 1

# 결과 출력
print(cnt)


# Please write your code here.

# # n　입력
# n = int(input())
# # password 입력
# password = list(map(int, input().split()))

# # 함수들
# # is_open(a, b, c)
# def is_open(a, b, c):
#     # 하나라도 차가 2 이하면 열림
#     return abs(a - password[0]) <= 2 or abs(b - password[1]) <= 2 or abs(c - password[2]) <= 2

# # 설계
# # cnt
# cnt = 0

# # 완전 탐색 시작
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             # 열리면,
#             if is_open(i, j, k):
#                 # cnt에 추가
#                 cnt += 1

# # 출력
# print(cnt)