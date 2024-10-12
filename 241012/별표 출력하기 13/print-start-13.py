# 변수 선언 및 입력
n = int(input())  # 사용자로부터 입력받기

# 총 2 * n줄에 대해 반복
for i in range(2 * n):
    if i % 2 == 0:  # 짝수 줄
        print("* " * n)  # n개의 별을 출력
    else:  # 홀수 줄
        print("* " * (n - (i // 2)))  # n에서 (i // 2)를 뺀 개수의 별을 출력