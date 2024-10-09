# import math

# def solution(a, b):
#     gcd_1920_2880 = math.gcd(1920, 2880)

#     for i in range(a, b+1):
#         if i % gcd_1920_2880 == 0:
#             print(1)
#             return True
#     print(0)


# a, b = map(int, input().split())
# solution(a,b)
# 변수 선언 및 입력
def solution(a, b):
    satisfied = False

    for i in range(a, b + 1):
        # a에서 b사이의 값 중 공약수가 있는지 확인합니다.
        if 1920 % i == 0 and 2880 % i == 0:
            satisfied = True
            break  # 공약수를 찾으면 더 이상 반복할 필요 없음

    # 출력
    if satisfied:
        print("1")
    else:
        print("0")

a, b = map(int, input().split())
solution(a, b)