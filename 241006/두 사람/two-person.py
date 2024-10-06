# 나이와 성별을 입력받기
A_y, A_s = map(str, input().split())
B_y, B_s = map(str, input().split())

# 나이를 정수형으로 변환
A_y = int(A_y)
B_y = int(B_y)

# 조건 확인
if (A_y >= 19 and A_s == "M") or (B_y >= 19 and B_s == "M"):
    print(1)
else:
    print(0)