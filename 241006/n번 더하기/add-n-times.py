# a, n = map(int, input().split())

# for i in range(i, n):
#     a += n  # a에 n을 더함
# print(i) 

# 정수 a와 n 입력 받기
a, n = map(int, input().split())

# a에 n을 더하는 과정을 n번 반복
for i in range(n):
    a += n  # a에 n을 더함
    print(a)  # 결과를 출력