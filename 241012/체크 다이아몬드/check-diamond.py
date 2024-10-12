def solution(n):
    # 위쪽 다이아몬드 부분
    for i in range(n):
        # 공백 출력
        print(" " * (n - i - 1), end="")
        # 별과 공백 번갈아 출력
        for j in range(i + 1):
            print("*", end=" ")
        print()  # 줄바꿈

    # 아래쪽 다이아몬드 부분
    for i in range(n - 1):
        # 공백 출력
        print(" " * (i + 1), end="")
        # 별과 공백 번갈아 출력
        for j in range(n - i - 1):
            print("*", end=" ")
        print()  # 줄바꿈

n = int(input())  # 사용자로부터 입력 받음
solution(n)