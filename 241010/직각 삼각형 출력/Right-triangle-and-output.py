def solution(n):
    for i in range(1, n + 1):  # i는 1부터 n까지
        # 각 줄마다 (2 * i - 1)개의 별을 출력
        print('*' * (2 * i - 1))

n = int(input())  # 사용자로부터 n 입력받기
solution(n)