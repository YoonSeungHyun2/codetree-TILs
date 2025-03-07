# n 입력
n = int(input())
# linear
linear = [0] * 101
# pos, alpha 입력
for _ in range(n):
    pos, alpha = input().split()
    # linear에 입력
    linear[int(pos)] = alpha

# 함수들
# exists(s, e)
def exists(s, e):
    
    # 양 끝에 사람이 있는지 반환
    return linear[s] and linear[e-1]

# only_g(s, e)
def only_g(s, e):
    
    # g_cnt
    g_cnt = 0

    # 현 범위 중
    for i in range(s, e):
        # 한 번이라도 'H'가 나오면
        if linear[i] == 'H':
            # 실패
            return False
    
    # 다 돌고나서
    # g_cnt 가 1 이상이면
    if g_cnt >= 1:
        # 성공
        return True
    
    # 이외에는 실패
    return False

# only_h(s, e):
def only_h(s, e):
    
    # h_cnt
    h_cnt = 0

    # 현 범위 중
    for i in range(s, e):
        # 한 번이라도 'G'가 나오면
        if linear[i] == 'G':
            # 실패
            return False
    
    # 다 돌고나서
    # h_cnt 가 1 이상이면
    if h_cnt >= 1:
        # 성공
        return True
    
    # 이외에는 실패
    return False

# same_g_h(s, e)
def same_g_h(s, e):
    
    # g_cnt, h_cnt
    g_cnt, h_cnt = 0, 0

    # 현 범위중
    for i in range(s, e):
        # 'G'가 나오면
        if linear[i] == 'G':
            # g_cnt 올려주기
            g_cnt += 1
        # 'H'가 나오면
        elif linear[i] == 'H':
            # h_cnt 올려죽
            h_cnt += 1
    
    # 갯수가 같은지 반환
    return g_cnt == h_cnt

# 설계
# max_len
max_len = 0

# 양 끝점 잡기
for i in range(1, 101):
    for j in range(i+1, 102):
        # 양 끝점에 사람이 있고, 오로지 G로 이루어져 있으면,
        if exists(i, j) and only_g(i, j):
            # max_len 업데이트
            max_len = max(max_len, j-i-1)
        # 양 끝점에 사람이 있고, 오로지 H로 이루어져 있으면,
        elif exists(i, j) and only_h(i, j):
            # max_len 업데이트
            max_len = max(max_len, j-i-1)
        # 양 끝점에 사람이 있고, G와 H가 정확히 같은 갯수만큼 있다면,
        elif exists(i, j) and same_g_h(i, j):
            # max_len 업데이트
            max_len = max(max_len, j-i-1)

# 출력
print(max_len)