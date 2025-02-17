a1, a2 = map(int, input().split())  # 두 정수 입력받기

int_list = [0] * 10  # 크기 10짜리 리스트 생성
int_list[0] = a1
int_list[1] = a2

for i in range(2, 10):
    int_list[i] = 2 * int_list[i - 2] + int_list[i - 1]  # 수열 생성

print(*int_list)  # 결과 출력
