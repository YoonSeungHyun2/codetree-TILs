for i in range(1, 4): 
    for j in range(1, 4):
        if i % 2 == 0:
            print(f"({i}, {j})", end="\n")
        else:
            print(f"({i}, {j})", end=" ")