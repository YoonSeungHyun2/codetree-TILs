# 입력받은 숫자 n
n = int(input())

# n 이하의 소수를 구하는 리스트 초기화 (모두 True로 설정)
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아니므로 False

# 에라토스테네스의 체 알고리즘
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:  # i가 소수인 경우
        for j in range(i * i, n + 1, i):  # i의 배수들을 소수가 아니라고 표시
            is_prime[j] = False

# 소수 출력
for i in range(2, n + 1):
    if is_prime[i]:
        print(i, end=" ")