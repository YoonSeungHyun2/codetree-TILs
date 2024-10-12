def draw_diamond(n):
    # 위쪽 다이아몬드 부분
    for i in range(n):
        # 공백 출력
        print(" " * (n - i - 1), end="")
        # 별 출력
        print("*" * (2 * i + 1))
    
    # 아래쪽 다이아몬드 부분
    for i in range(n - 1):
        # 공백 출력
        print(" " * (i + 1), end="")
        # 별 출력
        print("*" * (2 * (n - i - 1) - 1))

# 사용자로부터 n 입력받기
n = int(input())
draw_diamond(n)