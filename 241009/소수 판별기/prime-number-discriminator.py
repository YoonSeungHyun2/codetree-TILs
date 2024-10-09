def solution(n):
    satisfied = True

    for i in range(1, n+1):
        if n % i != 0:
            satisfied == False
    
    if satisfied == True:
        print("P")
    else:
        print("C")

n = int(input())
solution(n)