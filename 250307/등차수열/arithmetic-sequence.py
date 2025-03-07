# n = int(input())
# a = list(map(int, input().split()))

# # Please write your code here.

# n 입력
n = int(input())
# num_list 입력
num_list = list(map(int, input().split()))

# 함수들
# makes_ap(num_1, k, num_2)
def makes_ap(num_1, k, num_2):
    # num_1 - k 가 k - num_2가 같은지 반환
    return num_1 - k == k - num_2

# simulate(k)
def simulate(k):
    
    # curr_cnt
    curr_cnt = 0

    # 완전 탐색 시작
    for i in range(n-1):
        for j in range(i+1, n):
            # 두 수 사이에 k를 넣었을 때
            # 등차수열을 만족하면
            if makes_ap(num_list[i], k, num_list[j]):
                # curr_cnt 올려주기
                curr_cnt += 1
    
    # 반환
    return curr_cnt

# 설계
# min_num, max_num
min_num, max_num = min(num_list), max(num_list)

# max_cnt
max_cnt = 0

# 완전 탐색 시작
for i in range(min_num + 1, max_num):
    # max_cnt 업데이트
    max_cnt = max(max_cnt, simulate(i))

# 출력
print(max_cnt)