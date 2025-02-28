m1, d1, m2, d2 = map(int, input().split())

dates = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day1 = d1 + sum(days[:m1])
day2 = d2 + sum(days[:m2])

diff = (day2 - day1 + 1) % 7

# 음수 값 처리
if diff < 0:
    diff += 7

print(dates[diff])