n = int(input())  # 사용자로부터 n 입력받기

cnt = 1  # 시작 숫자

for i in range(n):
    if i % 2 == 0:  # 홀수 번째 줄 (0, 2, 4번째 줄)
        for j in range(n):
            print(cnt, end=" ")
            cnt += 1  # 1씩 증가
    else:  # 짝수 번째 줄 (1, 3, 5번째 줄)
        for j in range(n):
            print(cnt+1, end=" ")
            cnt += 2  # 2씩 증가
    print()  # 줄바꿈