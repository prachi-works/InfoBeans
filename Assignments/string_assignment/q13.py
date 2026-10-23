# 12. Check whether two strings are equal without using == for the complete strings.
s1='aabb'
s2='aabb'
if len(s1) != len(s2):
    print('Strings are not equal')
else:
    for i in range(len(s1)):
        if ord(s1[i])-ord(s2[i]):
            print('not equal')
            break
    else:
            print('string are equal')