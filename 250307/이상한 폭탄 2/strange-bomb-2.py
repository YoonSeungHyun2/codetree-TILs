# N, K = map(int, input().split())
# num = [int(input()) for _ in range(N)]

# # Please write your code here.

# n, k 입력
n, k = map(int, input().split())
# bombs
bombs = list()
# bombs 입력
for _ in range(n):
    bombs.append(int(input()))

# 설계
# max_num_bomb
max_num_bomb = -1

# 완전 탐색 시작
for i in range(n):
    for j in range(i+1, n):
        # 범위에 해당 되면서 같은 번호면
        if j - i <= k and bombs[i] == bombs[j]:
            # max_num_bomb 업데이트
            max_num_bomb = max(max_num_bomb, bombs[i])

print(max_num_bomb)