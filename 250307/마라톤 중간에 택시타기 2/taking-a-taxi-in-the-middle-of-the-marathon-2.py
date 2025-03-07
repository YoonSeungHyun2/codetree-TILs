# n 입력
n = int(input())
# check_points
check_points = []
# check_point 입력
for _ in range(n):
    x, y = map(int, input().split())
    check_points.append([x, y])

# 함수들
# simulate(k)
def simulate(k):
    
    # curr_dist
    curr_dist = 0

    # temp_check_points
    temp_check_points = []

    # check_points를 돌면서
    for i in range(n):
        # k번째를 제외한 check_point를 넣어줌
        if i == k:
            continue
        else:
            temp_check_points.append(check_points[i])
    
    # temp_check_points를 돌면서
    for i in range(n-2):
        # curr_dist에 추가
        curr_dist += abs(temp_check_points[i][0] - temp_check_points[i+1][0]) + abs(temp_check_points[i][1] - temp_check_points[i+1][1])

    # 반환
    return curr_dist
        
# 설계
# min_dist 설정
import sys
min_dist = sys.maxsize

# 1부터 n-2까지
for i in range(1, n-1):
    # min_dist 업데이트
    min_dist = min(min_dist, simulate(i))

# 출력
print(min_dist)