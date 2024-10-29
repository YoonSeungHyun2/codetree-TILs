# 변수 선언 및 입력
n = int(input())
cnt = 'A'  # 출력할 문자의 초기값 설정

# 알파벳을 삼각형 모양으로 출력
for i in range(n):
    # 줄의 시작에 공백 추가
    print("  " * i, end="")
    
    # 각 줄에 출력할 알파벳 수를 설정하여 출력
    for j in range(n - i):
        print(cnt, end=" ")
        # 알파벳을 다음 순서로 이동
        cnt = chr(ord(cnt) + 1)
        
        # Z를 넘어가면 A로 다시 돌아가도록 설정
        if ord(cnt) > ord('Z'):
            cnt = 'A'
    print()  # 줄바꿈