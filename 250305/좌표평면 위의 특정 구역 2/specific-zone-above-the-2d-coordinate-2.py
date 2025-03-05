# import sys

# # n 입력
# n = int(input())

# # 좌표 입력
# points = [tuple(map(int, input().split())) for _ in range(n)]
# x = [p[0] for p in points]
# y = [p[1] for p in points]

# # 최소 면적 초기화
# min_area = sys.maxsize

# # 한 점을 제외하고 직사각형 면적 계산
# for i in range(n):
#     # i 번째 좌표를 제외한 나머지 x, y 좌표 구하기
#     x_excluded = x[:i] + x[i+1:]
#     y_excluded = y[:i] + y[i+1:]

#     # 남은 점들의 최소 및 최대 x, y 좌표 찾기
#     max_x, min_x = max(x_excluded), min(x_excluded)
#     max_y, min_y = max(y_excluded), min(y_excluded)

#     # 면적 계산
#     area = (max_x - min_x) * (max_y - min_y)

#     # 최소 면적 업데이트
#     min_area = min(min_area, area)

# # 결과 출력
# print(min_area)


# -----------------------------------
# n 입력
n = int(input())
# pos_list
pos_list = list()
# pos_list 입력
for _ in range(n):
    pos_list.append(tuple(map(int, input().split())))

# 함수들
# calc(x, y)
def calc(x, y):
    
    # max_x, min_x, max_y, min_y
    max_x, min_x = -sys.maxsize, sys.maxsize
    max_y, min_y = -sys.maxsize, sys.maxsize

    # 해당 좌표를 제외한 좌표를 탐색
    for curr_x, curr_y in pos_list:
        
        # 해당 좌표라면
        if curr_x == x and curr_y == y:
            # 스킵
            continue
        
        # 아니라면
        else:
            # max_x, min_x 업데이트
            max_x, min_x = max(max_x, curr_x), min(min_x, curr_x)
            # max_y, min_y 업데이트
            max_y, min_y = max(max_y, curr_y), min(min_y, curr_y)
    
    # curr_area 생각해보니 음수 나올일 없음
    curr_area = (max_x - min_x) * (max_y - min_y)

    # 반환
    return curr_area
    
# 설계
# min_area
import sys
min_area = sys.maxsize

# 완전 탐색 시작
for x, y in pos_list:
    # x, y를 제외하고 면적 계산한값과 min_area를 비교하여 업데이트
    min_area = min(min_area, calc(x, y))

# 출력
print(min_area)