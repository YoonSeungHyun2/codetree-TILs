# 입력 받기
n = int(input())

# 배열을 생성하여 배수들을 저장
multiples = []

# 5의 배수가 나온 횟수를 저장할 변수
count_of_fives = 0

# 1부터 시작해서 배수 구하기
i = 1

while count_of_fives < 2:
    multiple = n * i
    multiples.append(multiple)  # 배열에 배수 추가
    print(multiple, end=' ')  # 배수 출력
    
    if multiple % 5 == 0:
        count_of_fives += 1  # 5의 배수이면 카운트 증가
    
    i += 1  # 다음 배수를 위한 값 증가

# 결과로 출력된 배열 확인 (필요시)
#print(multiples)
