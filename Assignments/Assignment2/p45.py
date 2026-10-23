# 45. Find the sum of 28 terms of an Arithmetic Progression -21 -18 -15 -12 . . . . .
# Given values 
first_term = -21
second_term = -18
n_terms = 28

#Find the common difference (d)
common_difference = second_term - first_term

#  Calculate the sum of n terms
# Formula: S_n = (n / 2) * (2 * a + (n - 1) * d)
sum_of_terms = (n_terms / 2) * (2 * first_term + (n_terms - 1) * common_difference)

print(f"Common Difference (d): {common_difference}")
print(f"Sum of first 28 terms: {int(sum_of_terms)}")
