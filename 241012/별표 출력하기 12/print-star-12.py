n = int(input())  # 사용자로부터 n 입력받기

for i in range(2 * n):  # 총 2n개의 줄에 대해 반복
    if i % 2 == 0:  # 짝수 줄
        print("* " * (2 * n - i))  # 별 출력
    else:  # 홀수 줄
        spaces = " " * (i // 2)  # 공백 생성
        print(spaces + "* " + spaces + "* " * ((2 * n - i) // 2 - 1))  # 홀수 줄 별 출력