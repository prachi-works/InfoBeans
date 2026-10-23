# 27. Group words that are anagrams of one another.
#     Example: ["eat", "tea", "bat", "ate"]
#     Expected groups: ["eat", "tea", "ate"] and ["bat"]
s = ["eat", "tea", "bat", "ate"]
result = {}

for word in s:
    key = ''.join(sorted(word))

    if key not in result:
        result[key] = []

    result[key].append(word)

print(result)

