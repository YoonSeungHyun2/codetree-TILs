# X, Y = map(int, input().split())

# # Please write your code here.

# x, y 입력
x, y = map(int, input().split())

# 함수들
# one_is_once(temp_list)
def one_is_once(temp_list):
    # 1이 존재하는지 반환
    return 1 in temp_list

# two_types_of_num(temp_list)
def two_types_of_num(temp_list):
    
    # used_num
    used_num = 0

    # 사용된 숫자를 조사
    for num in temp_list:
        # 사용되었으면
        if num:
            # used_num 올려주기
            used_num += 1
    
    # 두 가지 종류를 사용했는지 반환
    return used_num == 2

# is_interesting(k)
def is_interesting(k):

    # 0 ~ 9를 카운트 해줄 리스트
    temp = [0] * 10

    # k 탐색
    for i in k:
        # 숫자를 카운트
        temp[int(i)] += 1

    # 두 종류의 숫자를 사용하고, 그 중 하나가 한번만 사용되면
    if two_types_of_num(temp) and one_is_once(temp):
        # 성공
        return True
    
    # 이외는 실패
    return False

# 설계
# cnt
cnt = 0

# 완전 탐색 시작
for i in range(x, y + 1):
    # 흥미로운 숫자라면 (문자열로 인수 넘김)
    if is_interesting(str(i)):
        # cnt 올려주기
        cnt += 1

# 출력
print(cnt)