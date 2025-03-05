# n = int(input())
# A = list(map(int, input().split()))

# # Please write your code here.

# # 완전탐색 : 가능한 모든 경우에 대해서 해답을 찾아보는 방법
# # 시간복잡도 : O(N^2)
# # 각각 i번째 수를 2배로 한 경우
# # 모든 사람들의 이동거리를 구한다.

# 회의장소를 1 ~ N번까지 각각 위치 시켰을때

# 할거 한다.: 모든 사람들의 이동거리를 합한다.

# 위치시킨 회의 장소가 i

# for i in range(n):
#     # 할거 한다: 모든 사람들의 이동거리를 합한다.
#     dist = 0
#     for j in range(n):
#         # j번 위치 집에 있는 사람들의 이동거리 총합
#         # 이동거리 * j 위치에 있는 인구 수
#         #|i - j| * A_j
#         dist += abs(i - j) * A[j]

#     ans = min(a)
 
# -------------------------------------------------------- 
 # n 입력
n = int(input())
# ppl_list 입력
ppl_list = list(map(int, input().split()))

# 함수들
# search(k)
def search(k):
    
    # dist 설정
    dist = 0

    # 거리구하기
    for idx in range(n):
        dist += abs(idx - k) * ppl_list[idx]
    
    # 반환
    return dist

# 설계
# 최소 거리
import sys
short_cut = sys.maxsize

# 완전 탐색
for i in range(n):
    
    # 탐색
    curr_dist = search(i)

    # 최솟값 갱신
    short_cut = min(short_cut, curr_dist)

# 출력
print(short_cut)