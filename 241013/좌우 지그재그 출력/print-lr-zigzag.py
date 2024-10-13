n = int(input())  # 사용자로부터 n 입력받기

cnt = 1  # 숫자를 연속적으로 증가시키기 위한 변수

for i in range(1, n+1):  # 1부터 n까지 행 반복
    if i % 2 == 1:  # 홀수 번째 행
        for j in range(n):  # 숫자를 오름차순으로 출력
            print(cnt, end=" ")
            cnt += 1
    else:  # 짝수 번째 행
        start = cnt + n - 1  # 짝수 행에서는 역순으로 출력해야 하므로 시작값 설정
        for j in range(n):  # 숫자를 내림차순으로 출력
            print(start, end=" ")
            start -= 1
        cnt += n  # cnt를 다음 숫자로 이동
    print()  # 줄바꿈