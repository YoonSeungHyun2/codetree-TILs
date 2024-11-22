def main():
    arr = list(map(int, input().split()))

    # 조건: 리스트는 반드시 10개의 정수로 주어짐
    # if len(arr) != 10:
    #     print("Error: Please enter exactly 10 integers.")
    #     return

    # 짝수 번째 원소의 합 (1-based index 기준)
    even_sum = sum(arr[i] for i in range(1, len(arr), 2))  # 1-based 짝수는 0-based 홀수 위치

    # 3의 배수 번째 원소의 평균 (1-based index 기준)
    multiples_of_3 = [arr[i] for i in range(2, len(arr), 3)]  # 1-based 3의 배수는 0-based 2, 5, 8...
    if multiples_of_3:
        multiples_of_3_avg = round(sum(multiples_of_3) / len(multiples_of_3), 1)
    else:
        multiples_of_3_avg = 0.0  # 비어 있는 경우 평균은 0.0으로 처리

    # 결과 출력
    print(even_sum, multiples_of_3_avg)

if __name__ == "__main__":
    main()
