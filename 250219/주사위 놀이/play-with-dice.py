n = int(input())  # 정수 n 입력받기
numbers = list(map(int, input().split()))  # 한 줄의 입력을 정수 리스트로 변환

count_arr = [0] * 10  # 크기 10짜리 리스트 (0으로 초기화)

# 개수 세기
for num in numbers:
    count_arr[num] += 1

# 개수 출력
for i in range(1, 10):
    print(count_arr[i])
