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

import math

def solution(a, b):
    # 1920과 2880의 최대공약수를 구함
    gcd_1920_2880 = math.gcd(1920, 2880)  # 결과는 960
    
    # 범위 내에 gcd_1920_2880의 배수가 있는지 확인
    for i in range(a, b + 1):
        if i % gcd_1920_2880 == 0:
            print(0)  # 공약수가 존재함을 알림
            return
    
    # 공약수가 없으면 0 출력
    print(1)

# 입력 받기
a, b = map(int, input().split())
solution(a, b)