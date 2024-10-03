a = input()

arr = a.split("-")

m = int(arr[0])
d = int(arr[1])
y = int(arr[2])

print(f"{y}.{m}.{d}")

# # 날짜 입력받기
# a = input()  # 입력 형식: mm-dd-yyyy

# # 문자열을 '-'로 분리하여 리스트로 변환
# arr = a.split("-")

# # mm, dd, yyyy 각각 변수에 할당
# m = int(arr[0])  # 월
# d = int(arr[1])  # 일
# y = int(arr[2])  # 연도

# # 출력 형식으로 변환하여 출력
# print(f"{y}.{m}.{d}")