def solution():

    for i in range(n):
        for j in range(n - i): #왼쪽 * 출력
            print("*", end = "")
        for j in range(2 * i): # 가운데 공백 출력
            print(" ", end = "")
        for j in range(n - i): #오른쪽 * 출력
            print("*", end = "")
        print()


n = int(input())
solution()