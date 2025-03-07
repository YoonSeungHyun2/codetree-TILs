# n = int(input())
# times = [tuple(map(int, input().split())) for _ in range(n)]
# a = [t[0] for t in times]
# b = [t[1] for t in times]

# # Please write your code here.

# n　입력
n = int(input())
# work_time
work_time = list()
# work_time 입력
for _ in range(n):
    work_time.append(tuple(map(int, input().split())))

# 함수들
# calc(k)
def calc(k):
    
    # curr_time_table
    curr_time_table = [0] * 1001

    # 운행되고 있는 시간 체크
    for i in range(n):
        
        # 제외하는 인덱스일 경우
        if i == k:
            # skip
            continue
        
        # 이외의 경우
        # 언팩킹
        s, e = work_time[i]

        # 운행 시간 체크
        for j in range(s, e):
            curr_time_table[j] = 1
        
    # curr_total
    curr_total = sum(curr_time_table)
    
    # 반환
    return curr_total

# 설계
# max_time
max_time = 0

# 완전 탐색 시작
for i in range(n):
    # max_time 업데이트
    max_time = max(max_time, calc(i))

# 출력
print(max_time)