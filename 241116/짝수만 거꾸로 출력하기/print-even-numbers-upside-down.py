# 입력받기
n = int(input())  # 첫 번째 줄: 정수의 개수
numbers = list(map(int, input().split()))  # 두 번째 줄: n개의 정수

# 짝수만 선택하고 역순으로 출력
even_numbers = [num for num in numbers if num % 2 == 0]
print(" ".join(map(str, reversed(even_numbers))))
