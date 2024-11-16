scores = list(map(float, input().split()))  
# 한 줄에 입력된 점수를 실수형 리스트로 변환
average = sum(scores) / len(scores)


# 평균 학점을 소수 첫째 자리까지 반올림
average_rounded = round(average, 1)


# 출력
print(average_rounded)
