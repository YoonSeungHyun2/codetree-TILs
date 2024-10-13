# a, b = map(int, input().split())

# for i in range(1,10): 
#     for j in range(1, a):
#         print(f"{b} * {i*j} = {b * a}", end="")
#         if j < 10:
#             print(" /", end=" ")
#         print(f"{b-a} * {i*j} = {b * a}", end="")
#         if j < 10:
#             print(" /", end=" ")
#         print(f"{b-a} * {i*j} = {b * a}", end="")
#         if j < 10:
#             print(" /", end=" ")
#     print()

# 입력을 받습니다.
a, b = map(int, input().split())

# 큰 숫자부터 작은 숫자 순으로 짝수 구구단 출력
for j in range(1, 10):  # 1부터 9까지 구구단 출력
    result = []
    for i in range(b, a - 1, -2):  # b에서 a로 가며 짝수 구구단 출력
        result.append(f"{i} * {j} = {i * j}")
    print(" / ".join(result))  # 구구단 결과를 "/"로 연결하여 출력