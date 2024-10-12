# 입력 받기
n = int(input())

# (2n + 1) 크기의 패턴 생성
for i in range(2 * n + 1):
    if i % 2 == 0:  # 짝수 줄: 별을 모두 출력
        print("* " * (2 * n + 1))
    else:  # 홀수 줄: 별과 공백을 교차로 출력
        for j in range(2 * n + 1):
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # 다음 줄로 이동