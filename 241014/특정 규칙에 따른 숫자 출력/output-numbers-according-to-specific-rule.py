n = int(input())

cnt = 1
# 1부터 n까지의 수에 대해 역순으로 출력
for i in range(n):  # i는 0부터 n-1까지 반복
    print("  " * i, end="")  # 앞쪽에 i개의 공백 출력
    for j in range(n - i):  # n-i부터 1까지 숫자 출력
        print(cnt, end=" ")
        cnt += 1
        if cnt > 9:
            cnt = 1
    print()  # 줄 바꿈