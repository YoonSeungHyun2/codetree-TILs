# a, b, c, d = map(int, input().split())

# Please write your code here.

A, B, C, D = map(int, input().split())


h, m = A, B

h2, m2 = C, D

cnt = 0

while True:
    if h == h2 and m == m2:
        break

    m += 1
    cnt += 1
    if m == 60:
        h += 1
        m = 0

print(cnt)

# -------------------------

# while not (h == h2 and m == m2):
#     m += 1

#     if m == 60:
#         h += 1
#         m = 0

# -------------------------
# h, m = 2, 5

# h2, m2 = 4, 1

# print((60 * h2 + m2) - (60 * h + m))