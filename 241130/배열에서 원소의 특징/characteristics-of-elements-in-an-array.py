# 입력을 받아 리스트로 변환
numbers = list(map(int, input().split()))

# 3의 배수가 처음으로 등장하는 위치를 찾음
for i in range(1, len(numbers)):  # 인덱스 1부터 시작 (첫 번째 원소는 항상 3의 배수가 아님)
    if numbers[i] % 3 == 0:
        print(numbers[i - 1])  # 3의 배수의 바로 앞 원소 출력
        break

# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))

# 값을 하나씩 살펴보며 3의 배수가 처음으로 등장하는 부분을 찾고, 바로 앞 원소를 출력합니다.
for i in range(10):
    if arr[i] % 3 == 0:
        print(arr[i - 1])
        break