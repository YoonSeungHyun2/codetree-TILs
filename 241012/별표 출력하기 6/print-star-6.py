# def sol():

#     for i in range(n):
#         for j in range(n * i + 3):
#             print("*", end = " ")
#         for j in range(i):
#             print(" ", end = " ")
#         print()

#     for i in range(n * i - 3):
#         for j in range(i):
#             print("", end = " ")
#         for j in range(n * i + 3):
#             print("*", end = " ")
#         print()

# n = int(input())
# sol()

def solution(n):
    # 위쪽 삼각형 출력
    for i in range(n):
        # 공백 출력
        for j in range(i):
            print(" ", end=" ")
        # 별 출력
        for j in range((2 * n) - (2 * i) - 1):
            print("*", end=" ")
        print()
    
    # 아래쪽 삼각형 출력
    for i in range(n - 2, -1, -1):
        # 공백 출력
        for j in range(i):
            print(" ", end=" ")
        # 별 출력
        for j in range((2 * n) - (2 * i) - 1):
            print("*", end=" ")
        print()

# 사용자로부터 n 입력받기
n = int(input())
solution(n)