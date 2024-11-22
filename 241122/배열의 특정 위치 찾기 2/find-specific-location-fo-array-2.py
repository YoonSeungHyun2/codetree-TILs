arr = list(map(int, input().split()))

odd_sum = sum(arr[i] for i in range(0, len(arr), 2))  # 0-based 홀수 위치
even_sum = sum(arr[i] for i in range(1, len(arr), 2))

result = abs(odd_sum - even_sum)
print(result)
