#              1
#              ^
#              |      
#      2 <-- (/,\) --> 0 
#              | 
#              v
#              3

n = int(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y <n

def move(dir_now):
    if dir_now == 0:
        return [0, 1]
    elif dir_now == 1:
        return [-1, 0]
    elif dir_now == 2:
        return [0, -1]
    else:
        return [1, 0]

array = [[0 for i in range(n)]for j in range(n)] 

dir_state = 3

step = 1

#왼쪽에 머가 없다면 돈다.

x , y = (n-1)//2 , (n-1)//2

i = 0

array[x][y]=1

while True:
    #좌측 검사 포지션
    dir_state_left = dir_state + 1
    ldx, ldy = move(dir_state_left % 4)
    lx , ly = x + ldx , y + ldy
    #
    if n != 1 and array[lx][ly] == 0:
        dir_state += 1

    dx, dy = move(dir_state % 4)

    if in_range( x + dx ,y + dy) == True and array[x+dx][y+dy] == 0:
        # 가는 방향이 맞고 0으로 돼있다면 진행한다
        # 추가적으로 왼쪽에 숫자가 없다면 방향을 
        x , y = x + dx , y + dy
        step += 1

    array[x][y] = step
    if step >= n*n:
        break


    
for i in range(n):
    for j in range(n):
        print(array[i][j],end=" ")
    print()