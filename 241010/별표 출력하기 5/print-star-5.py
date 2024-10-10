def solution(n):
    for i in range(n):  # i는 현재 줄 번호
        # 각 줄마다 (n - i)개의 별을 n - i번 반복하여 출력
        for _ in range(n - i):
            print('*' * (n - i), end=' ')
        print()  # 각 줄이 끝나면 줄 바꿈

n = int(input())  # 사용자로부터 n 입력받기
solution(n)