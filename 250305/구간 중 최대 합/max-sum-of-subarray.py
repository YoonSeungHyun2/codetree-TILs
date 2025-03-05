# # n, k = map(int, input().split())
# # arr = list(map(int, input().split()))

# # Please write your code here.



# # n, k 입력
# n, k = map(int, input().split())
# # arr 입력
# arr = list(map(int, input().split()))

# # 모든 경우 : 가능한 모든 구간에 대해

# # 할 거 한다 : 구간의 최대값 구한다.

# # 함수들
# # calc(j)
# def calc(j):

#     # curr_sum
#     curr_sum = 0
#     for i in range(j, j+k):
#         curr_sum += arr[i]
    
#     # 반환
#     return curr_sum

# # 설계
# # max_sum
# max_sum = 0

# # 완전탐색
# for i in range(n - k + 1):
#     # max_sum 업데이트
#     max_sum = max(max_sum, calc(i))

# # 출력
# print(max_sum)

# ---------------

# n, k 입력
n, k = map(int, input().split())
# arr 입력
arr = list(map(int, input().split()))

# ---------------
ans = 0

for i in range(n-k+1):
    # 구간 내의 합을 구한다.
    value = sum (arr[i:i+k])

    ans = max(ans, value)

print(ans)
