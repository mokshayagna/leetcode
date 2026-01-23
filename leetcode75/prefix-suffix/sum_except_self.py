nums = [1,2,3,4]
n = len(nums)
t = [0]*n
for i in range(1,n): # [0,1,3,6]
    t[i] = t[i-1] + nums[i-1]
right = 0
for i in range(n-1,-1,-1):
    t[i] += right
    right += nums[i]
print(t)

