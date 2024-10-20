n = int(input())  # 사용자로부터 n 값을 입력받음

for i in range(1, n + 1):  # i는 1부터 n까지
    for j in range(1, n - i + 2):  # j는 1부터 n - i + 1까지
        print(f"{i} * {j} = {i * j}", end="")  # 구구단의 각 항목을 출력
        if j < n - i + 1:  # 마지막 항목이 아니라면 `/`로 구분
            print(" / ", end="")
    print()  # 각 i에 대해 줄을 바꿈 (다음 행으로 넘어가기 위해)