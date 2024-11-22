def main():
    arr = list(map(int, input().split()))  # 정수 배열 입력

    for i in range(len(arr)):
        if arr[i] == 0:  # 첫 번째로 등장하는 0 확인
            result = sum(arr[i - 3:i])  # 0 앞의 3개 숫자 합산
            print(result)
            break  # 첫 번째 0만 처리하므로 종료

if __name__ == "__main__":
    main()
