s = "abc"
t = "ahgdcb"

i = 0
j = len(t) - 1
for c in s:
    while i <= j and t[i] != c:
        i += 1
    if i > j:
        print(False)
        break
    i += 1
else:
    print(True) 
            