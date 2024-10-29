# 입력 처리: start와 end를 공백으로 구분하여 입력받음
start, end = map(int, input().split())

# 소수 판별 함수 정의
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 약수가 세 개인 수 찾기
count = 0
for num in range(start, end + 1):
    root = int(num**0.5)
    # num이 제곱수이고, 제곱근이 소수일 경우
    if root * root == num and is_prime(root):
        count += 1

# 결과 출력
print(count)