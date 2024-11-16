student = int(input())

pass_cun = 0

for _ in range(student):
    score = list(map(int, input().split()))

    average = sum(score) / 4

    if average >= 60:
        print("pass")
        pass_cun += 1 #
    else:
        print("fail")
print(pass_cun)
