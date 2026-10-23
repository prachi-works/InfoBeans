# *        *
#  *      *
#   *    *
#    *  *
#     *
#    *  *
#   *    *
#  *      *
# *        *
 
for i in range(1, 10):

    if i <= 5:
        n = i
    else:
        n = 10 - i

    for space in range(n - 1):
        print(" ", end="")

    print("*", end="")

    for space in range(2 * (5 - n)):
        print(" ", end="")

    if n != 5:
        print("*", end="")

    print()
