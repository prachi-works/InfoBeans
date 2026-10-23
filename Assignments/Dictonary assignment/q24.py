# 24. Group a list of words according to their length.
#     Example: ["cat", "apple", "dog", "mango"]
#     Expected groups: 3 -> ["cat", "dog"], 5 -> ["apple", "mango"]
l=["cat", "apple", "dog", "mango"]
res={len(element):[] for element in l}
for element in l:
    res[len(element)].append(element)
print(res)