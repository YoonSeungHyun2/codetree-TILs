from decimal import Decimal, getcontext

# 소수점 21자리 설정
getcontext().prec = 23  # 21자리 + 2자리(올림을 위한 여유)

a, b = map(int, input().split())

# Decimal을 사용하여 정확한 계산
n = Decimal(a) / Decimal(b)

# 소수점 21자리에서 내림하여 출력
print(f"{n:.20f}")