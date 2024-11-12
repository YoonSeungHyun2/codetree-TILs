arr = list(map(int, input().split()))

# 250 이하만 추출합니다.
even_arr = []
for num in arr:
    if num >= 250:
        break
    even_arr.append(num)

total_sum = sum(even_arr)
average = round(total_sum / len(even_arr), 1)
# 250 이하로만 이루어진 리스트
print(total_sum, average)

