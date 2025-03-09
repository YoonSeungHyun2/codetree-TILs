# N = int(input())
# x, y = map(int, input().split())

# grid = [["."] * (N + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#     row = input()
#     for j in range(1, N + 1):
#         grid[i][j] = row[j - 1]

# # Please write your code here.
# n 입력
n = int(input())
# sx, sy 입력
sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
# maze
maze = [
    input()
    for _ in range(n)
]

# 함수들
# next_is_empty_without_wall(x, y, d)
def next_is_empty_without_wall(x, y, d):
    # nx, ny
    nx, ny = x + dxs[d], y + dys[d]
    # nd
    nd = (d + 1) % 4
    # nxr, nyr
    nxr, nyr = nx + dxs[nd], ny + dys[nd]
    # 다음 위치가 범위 내에 있고, 비어 있으며, 다음 위치의 오른쪽 위치가 범위 내에 있고, 비어있는지 반환
    return in_range(nx, ny) and maze[nx][ny] == '.' and in_range(nxr, nyr) and maze[nxr][nyr] == '.' 

# next_is_empty_with_wall(x, y, d)
def next_is_empty_with_wall(x, y, d):
    # nx, ny
    nx, ny = x + dxs[d], y + dys[d]
    # nd
    nd = (d + 1) % 4
    # nxr, nyr
    nxr, nyr = nx + dxs[nd], ny + dys[nd]
    # 다음 위치가 범위 내에 있고, 비어 있으며, 다음 위치의 오른쪽 위치가 범위 내에 있고, 벽인지 반환
    return in_range(nx, ny) and maze[nx][ny] == '.' and in_range(nxr, nyr) and maze[nxr][nyr] == '#' 

# next_is_wall(x, y, d)
def next_is_wall(x, y, d):
    # nx, ny
    nx, ny = x + dxs[d], y + dys[d]
    # 범위 내에 있고, 벽인지 반환
    return in_range(nx, ny) and maze[nx][ny] == '#'

# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# can_out(x, y, d)
def can_out(x, y, d):
    # nx, ny
    nx, ny = x + dxs[d], y + dys[d]
    # 격자 밖인지 반환
    return not in_range(nx, ny)

# 설계
# dxs, dys
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
# curr_x, curr_y, curr_dir, t, dir_cnt, back_cnt
curr_x, curr_y, curr_dir, t, dir_cnt, back_cnt = sx, sy, 1, 0, 0, 0

# 시뮬레이션 시작
while True:
    
    # 탈출이면(현재방향으로 진행했을 때 격자 밖이면)
    if can_out(curr_x, curr_y, curr_dir):
        # 시간 올려주고
        t += 1
        # 출력 후
        print(t)
        # 반복분 종료
        break
    
    # 바라보는 방향으로 이동할 수 없으면(진행하려는 곳이 벽이면)
    elif next_is_wall(curr_x, curr_y, curr_dir):
        # 반시계방향으로 90도 회전
        curr_dir = (curr_dir - 1 + 4) % 4
        # dir_cnt 올려주기
        dir_cnt += 1
        # 연속으로 4번 바꾸면
        if dir_cnt == 4:
            # -1 출력 후
            print(-1)
            # 반복문 종료
            break
    
    # 바라보는 방향으로 이동할 수 있고, 이동한 후 오른쪽에 벽이 있으면
    elif next_is_empty_with_wall(curr_x, curr_y, curr_dir):
        # 움직여주고
        curr_x, curr_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
        # 시간 올려주고
        t += 1
        # dir_cnt 초기화
        dir_cnt = 0
        # 처음 위치로 돌아왔으면
        if curr_x == sx and curr_y == sy:
            # back_cnt 올려주기
            back_cnt += 1
            if back_cnt == 5:
                print(-1)
                break
    
    # 바라보는 방향으로 이동할 수 있고, 이동한 후 오른쪽에 벽이 없으면
    elif next_is_empty_without_wall(curr_x, curr_y, curr_dir):
        # 한칸 움직여주기
        curr_x, curr_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
        # 시간 올려주기
        t += 1
        # 시계방향으로 90도 회전
        curr_dir = (curr_dir + 1) % 4
        # 또 한칸 움직여주기
        curr_x, curr_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
        # 시간 올려주기
        t += 1
        # dir_cnt 초기화
        dir_cnt = 0
        # 처음 위치로 돌아왔으면
        if curr_x == sx and curr_y == sy:
            # back_cnt 올려주기
            back_cnt += 1
            if back_cnt == 5:
                print(-1)
                break