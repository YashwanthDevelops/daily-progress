# s = "A man, a plan, a canal: Panama"
# s.lower()
# s1 = []
# for i in s:
#     ascii = ord(i)
#     if 65 <= ascii <= 90 or 97 <= ascii <= 122:
#         s1.append(i)
# s2 = list(s1)
# s2.reverse()

# print(s1)
# print(s2)
# if(s1 == s2):
#     print(True)
# else:
#     print(False)


s = "0P"
s = s.lower()
s1 = []
for i in s:
    ascii = ord(i)
    if i.isalnum():
        s1.append(i.lower())
s2 = list(s1)
s2.reverse()
if(s1 == s2 ):
    print(True)
else:
    print(False)