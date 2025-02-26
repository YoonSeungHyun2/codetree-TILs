n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]  # 최댓값을 배열의 첫 번째 원소로 초기화
current_sum = arr[0]  # 현재 연속된 부분 수열의 합

for i in range(1, n):
    current_sum = max(arr[i], current_sum + arr[i])  # 현재 원소부터 시작할지, 기존 합에 더할지 결정
    max_sum = max(max_sum, current_sum)  # 최대 부분 합 갱신

print(max_sum)
