a, b = map(int, input().split())  # 입력받기

while a <= b:  # a가 b보다 작거나 같을 때까지 반복
    print(a, end=" ")  # 현재 숫자 출력
    
    if a % 2 == 0:  # 짝수인 경우
        a += 3  # 3을 더함
    else:  # 홀수인 경우
        a *= 2  # 2배로 증가