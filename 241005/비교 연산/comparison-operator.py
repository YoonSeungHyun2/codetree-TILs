# 두 정수 입력받기
a, b = map(int, input().split())

# 각 조건에 대한 결과를 출력
print(1 if a >= b else 0)  # a가 b보다 같거나 큰가?
print(1 if a > b else 0)   # a가 b보다 큰가?
print(1 if b >= a else 0)  # b가 a보다 같거나 큰가?
print(1 if b > a else 0)   # b가 a보다 큰가?
print(1 if a == b else 0)  # a와 b가 같은가?
print(1 if a != b else 0)  # a와 b가 다른가?