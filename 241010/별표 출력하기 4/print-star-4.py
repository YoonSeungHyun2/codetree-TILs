def solution():
    for i in range(n):
        for j in range(n - i):
            print("*", end = " ")
        print()

    for i in range(1,  n):
        for j in range(i + 1):
            print("*", end = " ")
        print()
n = int(input())
solution()

# def solution(n):
#     # 첫 번째 부분: 별을 감소시키는 부분
#     for i in range(n):
#         for j in range(n - i):
#             print("*", end=" ")
#         print()  # 줄 바꿈

#     # 두 번째 부분: 별을 증가시키는 부분
#     for i in range(1, n):
#         for j in range(i + 1):
#             print("*", end=" ")
#         print()  # 줄 바꿈

# n = int(input())  # 사용자로부터 n 입력받기
# solution(n)