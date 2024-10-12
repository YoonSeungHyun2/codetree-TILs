n = int(input())  # 사용자로부터 n 입력받기

for i in range(1, n + 1):  # 1부터 n까지 반복
    if i == 1:
        print("* " * n)  # 첫 번째 줄은 n개의 별 출력
    else:
        for k in range(1, n + 1):  # n개의 열에 대해 반복
            if k < i:
                print("* ", end="")  # k가 i보다 작으면 별 출력
            elif k == n:
                print("* ", end="")  # 마지막 열에 별 출력
            else:
                print("  ", end="")  # 그 외에는 공백 출력
        print()  # 줄바꿈