# n, c, g, h 입력
n, c, g, h = map(int, input().split())
# preference_list
preference_list = list()
# preference_list 입력
for _ in range(n):
    preference_list.append(tuple(map(int, input().split())))

# 함수들
# calc(celcious, ta, tb)
def calc(celcious, ta, tb):
    # 현재 온도가 ta보다 작다면
    if celcious < ta:
        # c 반환
        return c
    
    # 현재 온도가 ta이상 tb 이하라면
    elif ta <= celcious <= tb:
        # g 반환
        return g
    
    # 현재 온도가 tb 초과라면
    else:
        # h 반환
        return h

# simulate(celcious)
def simulate(celcious):
    
    # curr_work
    curr_work = 0

    # 모든 기계를 탐색
    for i in range(n):
        
        # unpacking
        ta, tb = preference_list[i]

        # 현재온도에서 각 기계의 작업량을 curr_work에 추가
        curr_work += calc(celcious, ta, tb)
    
    # curr_work 반환
    return curr_work

# 설계
# max_work
max_work = 0

# 완전 탐색 시작 -> 0도부터 1000도까지
for celcious in range(1001):
    # max_work 업데이트
    max_work = max(max_work, simulate(celcious))

# 출력
print(max_work)