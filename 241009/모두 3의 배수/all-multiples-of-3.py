def solution():
    satisfied = True  # 모든 수가 3의 배수인지 확인할 변수

    for _ in range(5):  # 5개의 숫자를 입력받기 위한 반복문
        number = int(input())  # 숫자를 입력받음
        if number % 3 != 0:  # 3의 배수가 아닐 경우
            satisfied = False  # 변수 값 변경
            break  # 반복문 종료

    # 모든 수가 3의 배수일 경우 1 출력, 그렇지 않으면 0 출력
    if satisfied == True:
        print(1)
    else:
        print(0)

# 함수 호출
solution()