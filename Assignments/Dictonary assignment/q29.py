#  29. Given two dictionaries, return the keys whose values are equal in both.
d1={'a':1,'b':2,'c':3}
d2={'d':1,'b':2,'e':4}

for key,value in d1.items():
    if key in d2 and value==d2[key]:
        print(key)
