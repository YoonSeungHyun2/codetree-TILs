# 입력
s = input()

# 설계
# 정답 설정
ans = 0
for i in range(len(s) - 1):
    # '(('를 찾으면
    if s[i] == '(' and s[i+1] == '(':
        # 이후에 '))'가 있는지 확인
        for j in range(i+2, len(s) - 1):
            # 있으면
            if s[j] == ')' and s [j+1] == ')':
                # ans 추가
                ans += 1
# 출력
print(ans)