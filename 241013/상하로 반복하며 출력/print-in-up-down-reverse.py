n = int(input())  # 사용자로부터 n 입력받기

for i in range(1, n+1):  # 1부터 n까지 행 반복
    for j in range(1, n+1):  # 1부터 n까지 열 반복
        if j % 2 == 1:  # 홀수 번째 열에서는 해당 행 번호 출력
            print(i, end="")
        else:  # 짝수 번째 열에서는 n - i + 1 출력
            print(n - i + 1, end="")
    print()  # 줄바꿈