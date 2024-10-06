sex = int(input())
year = int(input())


if sex == 0 and year >= 19:
    print("MAN")
elif sex == 1 and year >= 19:
    print("WOMAN")
elif sex == 0 and year < 19:
    print("BOY")
else:
    print("GIRL")