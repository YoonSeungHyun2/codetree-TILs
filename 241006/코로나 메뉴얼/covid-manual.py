# 검사자 정보를 저장할 리스트
coughs = []
temperatures = []

# 각 검사자에 대한 입력 받기
for _ in range(3):
    symptom, temp = input().split()  # 감기 증상과 체온 입력 받기
    coughs.append(symptom)            # 증상 리스트에 추가
    temperatures.append(int(temp))    # 체온 리스트에 추가

# A로 가는 사람 수 카운트
A_count = 0

# 각 검사자의 상태를 확인
for i in range(3):
    if coughs[i] == "Y" and temperatures[i] >= 37:
        A_count += 1  # 증상 있음, 체온 37℃ 이상 => A

# A_count가 2 이상일 때 위급상황
if A_count >= 2:
    print("E")  # 위급상황
else:
    print("N")  # 위급상황이 아님