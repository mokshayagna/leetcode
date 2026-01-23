word1 = "abc"
word2 = "pqr"
"""
    b = " ".join(word1)
    for i in word2:
        if " " in b:
            b = b.replace(" ",i,1)
        else:
            b = b + i
    b = b.replace(" ","")
    print(b)
"""
# TWO POINTER FORMULA #
i = 0
j = 0
result = ""
while i < len(word1) and j < len(word2):
    result += word1[i]
    result += word2[j]
    i += 1
    j+= 1
if i < len(word1):
    result += word1[i:] 
if j < len(word2):
    result += word2[i:] 
print(result)

