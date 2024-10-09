def solution (a, b, c):

    satisfied = True
    for i in range(a, b+1):
        if i % c == 0:
            satisfied = False

    if satisfied == True:
        print("YES")
    else:
        print("NO")

a, b, c = map(int, input().split())
solution(a, b, c)