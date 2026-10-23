
# 44. Find the 28th term of an Arithmetic Progression -21 -18 -15 -12 . . . . . 
first_term= -21
second_term = -18
difference = second_term - first_term
no_of_term= 28


print(f"The common difference between the term is(d): {difference}")
twenty_eight_term= first_term + (no_of_term - 1) * difference 
print(f"The 28 term is {twenty_eight_term}")