# n = int(input())
# cnt = 0

# for i in range(1, n+1):
#     if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#         continue
#     cnt += 1
# print(cnt)      

n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue  # 친근한 수는 넘어감
    cnt += 1  # 친근하지 않은 수의 개수 증가

print(cnt)