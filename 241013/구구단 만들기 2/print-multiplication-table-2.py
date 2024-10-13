a, b = map(int, input().split())

# 큰 숫자부터 작은 숫자 순으로 짝수 구구단 출력
for j in range(a, 10, a): 
    result = []
    for i in range(b, 1, -1):  
        result.append(f"{i} * {j} = {i * j}")
    print(" / ".join(result))