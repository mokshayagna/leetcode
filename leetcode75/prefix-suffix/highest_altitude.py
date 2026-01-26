a = [-5,1,5,0,-7]
'''
res = [0]
for i in range(1, len(a)):
    res.append(a[i-1]+res[i-1])
print(max(res))
'''
 
curr = 0
highest = 0

for gain in a:
    curr = curr + gain
    highest = max(highest, curr)
print(highest)
