# 정수 a, b 입력받기
a, b = map(int, input().split())

# b단부터 a단까지 출력
for j in range(2, 10, 2):  # 2, 4, 6, 8을 곱하기
    result = []
    for i in range(b, a - 1, -1):  # b단에서 a단까지 감소
        result.append(f"{i} * {j} = {i * j}")  # 구구단 형식으로 저장
    print(" / ".join(result))  # 결과를 '/'로 연결하여 출력