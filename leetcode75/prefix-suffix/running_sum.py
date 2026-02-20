s = [1,2,3,4]
# O/P = [1,3,6,10]
n = len(s)
t = [0]*n
t[0] = s[0]
for i in range(1,n): 
    t[i] = t[i-1] + s[i]
print(t)
