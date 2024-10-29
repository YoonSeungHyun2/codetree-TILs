# 첫 번째 줄에 m 입력
m = int(input())

# m번 반복해서 자연수 n을 입력받고 콜라츠 수열 반복 횟수 계산
for _ in range(m):
    n = int(input())
    steps = 0  # 반복 횟수 초기화
    
    # n이 1이 될 때까지 반복
    while n != 1:
        if n % 2 == 0:
            n //= 2  # 짝수면 2로 나눔
        else:
            n = 3 * n + 1  # 홀수면 3을 곱하고 1을 더함
        steps += 1  # 반복 횟수 증가

    # 결과 출력
    print(steps)