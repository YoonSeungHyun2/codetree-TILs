y = int(input())

if (y % 4 == 0 and y % 100 != 100) or (y % 400 == 0):
    print("true")
else:
    print("false")

#     # 윤년 판단
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#     print("윤년입니다.")
# else:
#     print("평년입니다.")