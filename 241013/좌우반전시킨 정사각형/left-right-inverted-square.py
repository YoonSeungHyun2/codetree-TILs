n = int(input())

for i in range(1, n+1):  # n에서 1까지 감소하는 반복문 (행)
    for j in range(n, 0, -1):  # n에서 1까지 감소하는 반복문 (열)
        print(j*i, end=" ")  # (i,j) 형태로 출력
    print()  # 줄바꿈