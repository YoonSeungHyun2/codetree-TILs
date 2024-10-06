A_c, A_t = input().split()
B_c, B_t = input().split()
C_c, C_t = input().split()

A_t = int(A_t)
B_t = int(B_t)
C_t = int(C_t)

# 각 검사자의 증상 여부를 리스트로 저장
coughs = [A_c, B_c, C_c]
temperatures = [A_t, B_t, C_t]

A_count = 0

for i in range(3):
    if coughs[i] == "Y" and temperatures[i] >= 37:
        A_count += 1  # A로 분류
    elif coughs[i] == "N" and temperatures[i] >= 37:
        print("B")
    elif coughs[i] == "Y" and temperatures[i] < 37:
        print("C")

# A_count가 2 이상일 때 위급상황
if A_count >= 2:
    print("E")
else:
    print("N")