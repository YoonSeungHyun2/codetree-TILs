# n = int(input())
# blocks = [int(input()) for _ in range(n)]
# s1, e1 = map(int, input().split())
# s2, e2 = map(int, input().split())

# # Please write your code here.
# n 입력
n = int(input())
# jenga 입력
jenga = [
    int(input())
    for _ in range(n)
]
# take_outs 입력
take_outs = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

# 함수들
# eliminate(s_p, e_p)
def eliminate(s_p, e_p):
    
    # 전역 변수 선언
    global jenga

    # temp
    temp = []

    # curr_len
    curr_len = len(jenga)

    for i in range(curr_len):
        # 제거하는 범위 내면,
        if s_p <= i < e_p:
            # skip
            continue
        # 제거하는 범위 밖이면,
        else:
            # temp에 추가
            temp.append(jenga[i])
    
    # jenga 바꿔주기
    jenga = temp

# 설계
for take_out in take_outs:
    # unpacking
    s, e = take_out
    # 제거하기
    eliminate(s-1, e)

# 출력
print(len(jenga))
for j in jenga:
    print(j)