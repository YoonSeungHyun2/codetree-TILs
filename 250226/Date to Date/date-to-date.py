# 2011년 각 월별 일 수 (윤년 아님)
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# 입력 받기
A_month, A_day, C_month, C_day = map(int, input().split())  # 시작 월, 일 / 종료 월, 일

# 현재 날짜 설정
m, d = A_month, A_day
cnt = 0

while True:
    cnt += 1  # 하루 증가 (마지막 날 포함)

    if m == C_month and d == C_day:
        break  # 종료 날짜 도달 시 종료

    d += 1  # 하루 증가

    if d > days_in_month[m]:  # 해당 월의 마지막 날짜를 초과하면 다음 달로 변경
        d = 1
        m += 1

print(cnt)
