arr = list(map(int, input().split()))

filtered_arr = []
for num in arr:
    if num == 0:
        break
    filtered_arr.append(num)

print(" ".join(map(str, reversed(filtered_arr))))