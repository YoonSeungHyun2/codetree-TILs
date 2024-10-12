n = int(input())  # 사용자로부터 n 입력받기

for i in range(n):  # n개의 줄에 대해 반복
    if i % 2 == 0:  # 짝수 줄 (0, 2, ...)
        print("* " * (n - i // 2))  # 별 출력
    else:  # 홀수 줄 (1, 3, ...)
        spaces = " " * (i // 2 * 2)  # 공백 생성
        print("* " + spaces + "* " * ((n - i) // 2))  # 별과 공백 출력