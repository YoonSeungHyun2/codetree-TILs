n = int(input())  # 정수 n 입력받기

a, b = 1, n  # 첫 번째 항: 1, 두 번째 항: n
sequence = [a, b]  # 결과 저장 리스트

while True:
    next_term = a + b  # 다음 항 계산
    sequence.append(next_term)  # 리스트에 추가
    if next_term > 100:  # 100을 넘으면 종료
        break
    a, b = b, next_term  # 값 업데이트

print(*sequence)  # 공백으로 구분해 출력
