# 33. Check whether a string has balanced parentheses.[Stack]
# Example: "{[()]}" → True, "([)]" → False
s='{[()]}'
d = {"{":"}","[":"]","(":")"}
stack = []


# for ele in s:
#   if ele in d:
#     if ele == "{":
#       l1.append(d["{"])
#     elif ele == "[":
#       l1.append(d["["])
#     else :
#       l1.append(d["("])
#   else :
#     if ele != l1.pop():
#       print(False)
#       break
# else :
#   print(True)


for element in s:
    #check every character for
    if element in d:
        stack.append(d[element])
    else:
        if not stack or element != stack.pop(): #pop method pop from last 
            # not l1 checks whether the list is empty before attempting to remove an element.
            # ele != l1.pop() checks whether the current closing bracket matches the expected closing bracket
            print(False)
            break
else:    # Runs after the loop finishes without break
     print(len(stack)==0)