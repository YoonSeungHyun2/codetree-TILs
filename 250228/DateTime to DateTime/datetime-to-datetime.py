# 기준 시간 (2011년 11월 11일 11시 11분)
base_day, base_hour, base_minute = 11, 11, 11

# 입력값 받기
A, B, C = map(int, input().split())

# 주어진 시간이 기준 시간보다 앞선다면 -1 출력
if (A, B, C) < (base_day, base_hour, base_minute):
    print(-1)
else:
    # 기준 시간부터 주어진 시간까지의 차이를 분 단위로 계산
    total_minutes = ((A - base_day) * 24 * 60) + ((B - base_hour) * 60) + (C - base_minute)
    print(total_minutes)
