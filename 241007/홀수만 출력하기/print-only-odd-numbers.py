# 첫 번째 줄에 정수 N을 입력받습니다.
N = int(input())

# N개의 정수를 저장할 리스트를 만듭니다.
numbers = []

# N개의 정수를 입력받아 리스트에 저장합니다.
for _ in range(N):
    number = int(input())
    numbers.append(number)

# 홀수이면서 3의 배수인 수를 출력합니다.
for num in numbers:
    if num % 2 != 0 and num % 3 == 0:  # 홀수이면서 3의 배수인지 확인
        print(num)  # 조건에 맞는 숫자를 출력