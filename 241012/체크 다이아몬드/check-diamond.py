def solution(n):
    # 위쪽 다이아몬드 부분
    for i in range(n):
        # 공백 출력
        for j in range(n - i - 1):
            print(" ", end="")
        # 별 출력
        for j in range(i + 1):
            print("* ", end="")  # 별 사이에 공백 추가
        print()  # 줄바꿈

    # 아래쪽 다이아몬드 부분
    for i in range(n-2, -1, -1):
        # 공백 출력
        for j in range(n - i - 1):
            print(" ", end="")
        # 별 출력
        for j in range(i + 1):
            print("* ", end="")  # 별 사이에 공백 추가
        print()  # 줄바꿈

# 입력 값 처리
n = int(input())  # 사용자로부터 입력 받음
solution(n)