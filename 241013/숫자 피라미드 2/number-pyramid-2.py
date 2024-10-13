n = int(input())
cnt = 1
# 1부터 n까지의 수에 대해 피라미드 출력
for i in range(1, n + 1):  # 1부터 n까지의 줄
    for j in range(i):  # i개만큼의 숫자 출력
        print(cnt, end=" ")  
        cnt += 1
    print()  # 줄 바꿈