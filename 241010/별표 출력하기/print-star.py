def solution(n):
    for i in range(n): 
        for j in range(i + 1):
            print("*", end=" ")
        print()

    for i in range(n - 1): 
        for j in range(n - 1 - i):
            print("*", end=" ")
        print()


n = int(input())  # 사용자로부터 n 입력받기
solution(n)