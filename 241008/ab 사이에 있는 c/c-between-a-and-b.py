def solution(a, b, c):
    for i in range(a, b+1):
        if i % c == 0:
            print("YES")
            return
    print("NO")

# n을 입력받기
a, b, c = map(int, input().split())
solution(a, b, c)