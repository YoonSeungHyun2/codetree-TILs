n = int(input())

cnt_2 = 0
cnt_3 = 0
cnt_12 = 0

for i in range(1, n+1):
    if i % 12 == 0:
        cnt_12 += 1
    elif i % 3 == 0:
        cnt_3 += 1
    elif i % 2 == 0:
        cnt_2 += 1
    
    
print(cnt_2, cnt_3, cnt_12)

# ##
# 2일마다 교실청소
# 3일마다 복도청소
# 12일마다 화장실 청소
# for 문을 통해 돌게 하는데 각 카운트를 2,3,12로 정하자