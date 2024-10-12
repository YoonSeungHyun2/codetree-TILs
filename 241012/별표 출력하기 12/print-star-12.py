n = int(input())  # 사용자로부터 n 입력받기

for i in range(n):  # n개의 줄에 대해 반복
    if i == 0:  # 첫 번째 줄
        print("* " * n)  # n개의 별 출력
    else:  # 1부터 n-1까지
        print(" " * i + "* " + " " * (n - 1 - i) * 2 + ("* " if i < n - 1 else ""))  # 별 출력