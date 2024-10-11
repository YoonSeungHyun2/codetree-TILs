def solution ():
    for i in range(n): 
        for j in range(i):
            print(" ", end=" ")
        
        for j in range((2 * n) - (2 * i) - 1):
            print("*", end=" ")
        print()

n = int(input())
solution()

# def solution():
#     for i in range(n):
#         # 첫 번째 루프: i개의 공백 출력
#         for j in range(i):
#             print(" ", end=" ")

#         # 두 번째 루프: (2 * n - 2 * i - 1)개의 별 출력
#         for j in range((2 * n) - (2 * i) - 1):
#             print("*", end=" ")

#         # 각 줄 출력 후 줄 바꿈
#         print()

# n = int(input())  # 사용자로부터 n 입력받기
# solution()