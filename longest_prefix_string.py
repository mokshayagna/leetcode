a = ["flower","flow","flight"]
res = ""
for i in range(len(a[0])):
    ch = a[0][i]
    for w in a:
        if w[i] != ch or i >= len(w):
            print(res)
            exit()
    res += ch
print(res)
