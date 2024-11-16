# 입력: 과목 수와 학점
n = int(input())  # 첫 번째 줄: 과목 수 입력
grades = list(map(float, input().split()))  # 두 번째 줄: 학점 입력

# 평균 학점 계산
average = sum(grades) / n

# 평균 학점을 소수 첫째 자리까지 반올림
average_rounded = round(average, 1)

# 등급 판단
if average_rounded >= 4.0:
    grade = "Perfect"
elif average_rounded >= 3.0:
    grade = "Good"
else:
    grade = "Poor"

# 출력
print(average_rounded)
print(grade)
