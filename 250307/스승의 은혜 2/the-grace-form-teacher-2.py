# N, B = map(int, input().split())
# P = [int(input()) for _ in range(N)]

# # Please write your code here.

# n, b 입력
n, b = map(int, input().split())
# price_list
price_list = list()
# price_list 입력
for _ in range(n):
    price_list.append(int(input()))

# 함수들
# simulate(idx)
def simulate(idx):

    # temp -> price_list 복사
    temp = price_list[:]

    # 현재 idx의 가격을 반값으로 바꿔주기
    temp[idx] = price_list[idx] / 2

    # temp 정렬
    temp.sort()

    # curr_students
    curr_students = 0

    # 가장 작은 가격부터 탐색 시작
    for i in range(n+1):
        
        # curr_value
        curr_value = sum(temp[:i])
        
        # curr_value가 예산 내에 있으면,
        if curr_value <= b:
            # curr_stuednts 업데이트
            curr_students = i
    
    # 반환
    return curr_students

# 설계
# max_students
max_students = 0

# 완전 탐색 시작
for i in range(n):
    # 현재 인덱스를 반값으로 내려서,
    # 몇개까지 살 수 있는지 확인하는 시뮬레이션을 돌려,
    # max_students 업데이트
    max_students = max(max_students, simulate(i))

# 출력
print(max_students)
