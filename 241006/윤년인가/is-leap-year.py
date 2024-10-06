# y = int(input())

# if (y % 4 == 0):
#     print("true")
# elif (y % 100 == 0) and (y % 400 != 0):
#     print("false")
# else:
#     print("false")

# 자연수 y를 입력받습니다.
y = int(input())

# 윤년 판단
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("true")
else:
    print("false")