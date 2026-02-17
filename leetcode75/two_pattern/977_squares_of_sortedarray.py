nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

res = []
for i in nums:
    res.append(i*i)
print(sorted(res))

"""
i = 0
j = len(nums) - 1
res = [0] * len(nums)
while i <= j:
    if abs(nums[i]) > abs(nums[j]):
        res[j - i] = nums[i] * nums[i]
        i += 1
    else:
        res[j - i] = nums[j] * nums[j]
        j -= 1
print(res)
"""
