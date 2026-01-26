nums = [1,2,3,4]
"""
n = len(nums)
t = [0]*n
for i in range(1,n): # [0,1,3,6]
    t[i] = t[i-1] + nums[i-1]
right = 0
for i in range(n-1,-1,-1):
    t[i] += right
    right += nums[i]
print(t)
"""

### BRUTE FORCE APPROACH ###
"""
nums = [1,2,3,4]

ans = [0] * len(nums)

for i in range(len(nums)):
    total = 0
    for j in range(len(nums)):
        if i != j:
            total += nums[j]
    ans[i] = total

print(ans)   

"""

### PREFIX ###
prefix = [0] * len(nums)
for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] + nums[i-1]
print(prefix)

### SUFFIX ###
suffix = [0] * len(nums)
length = len(nums)
for i in range(length-2,-1,-1):
    suffix[i] = suffix[i+1] + nums[i+1]
print(suffix)
    
total = [0] * len(nums)
for i in range(len(nums)):
    total[i] = prefix[i] + suffix[i]
print(total)
