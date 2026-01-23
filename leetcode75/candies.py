candies = [2,3,5,1,3]
extra_Candies = 3
can = []
res = max(candies)
for i in range(len(candies)):
    if candies[i] + extra_Candies >= res:
        can.append(True)
    else:
        can.append(False)
print(can)
        
