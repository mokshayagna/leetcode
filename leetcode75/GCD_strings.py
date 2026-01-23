import math
str1 = "ABCABC"
str2 = "ABC"
if str1+str2 == str2+str1:
    b = math.gcd(len(str1),len(str2))
    res = str1[:b]
print(b)
print(res)

