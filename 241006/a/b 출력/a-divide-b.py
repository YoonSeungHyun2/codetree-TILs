from decimal import Decimal, getcontext, ROUND_DOWN

# 소수점 21자리 설정
getcontext().prec = 23  # 21자리 + 2자리(올림을 위한 여유)

a, b = map(int, input().split())

# Decimal을 사용하여 정확한 계산
n = Decimal(a) / Decimal(b)

# 소수점 21자리에서 내림 처리
n = n.quantize(Decimal('0.00000000000000000001'), rounding=ROUND_DOWN)

# 소수점 21자리 출력
print(n)