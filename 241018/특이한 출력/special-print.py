n = int(input())  # 사용자로부터 n 값을 입력받음

for i in range(1, n + 1):  # i는 1부터 n까지
    for j in range(1, n + 1):  # j는 1부터 n까지
        print(f"({i}, {j})", end=" ")  # 각 좌표를 출력
        if (i + j) % 4 == 0:  # i + j가 4의 배수이면
            print()  # 줄을 바꿈
    # print()  # 각 i에 대해 줄을 바꿈 (다음 행으로 넘어가기 위해)