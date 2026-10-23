for i in range(1, 6):

    for j in range(1, 10):

        if (j == 5 - i or j == 5 + i or
            (i == 3 and j >= 3 and j <= 7)):
            print("*", end="")
        else:
            print(" ", end="")

    print()