# x, y 입력
x, y = map(int, input().split())

# 함수들
# calc(k)
def calc(k):
    
    # curr_sum
    curr_sum = 0

    # str_k
    str_k = str(k)

    for i in str_k:
        curr_sum += int(i)
    
    # 반환
    return curr_sum


# 설계
max_sum = 0

# 완전 탐색 시작
for i in range(x, y+1):

    # max_sum 업데이트
    max_sum = max(max_sum, calc(i))

# 출력
print(max_sum)