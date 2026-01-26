nums = [1,7,3,6,5,6]
n = len(nums)
"""
# Step1: build prefix sum
left = [0]*n
left[0] = 0

for i in range(1, n):
    left[i] = left[i-1] + nums[i-1]

# Step2: compute total sum (can also get from prefix)
total = sum(nums)

# Step3: find pivot index
for i in range(n):
    right = total - left[i] - nums[i]
    if left[i] == right:
        print("Pivot:", i)
        break
"""
prefix = [0]*n
for i in range(1,n):
    prefix[i] = prefix[i-1] + nums[i-1]
total = sum(nums)
for i in range(n):
    if prefix[i] == total - prefix[i] - nums[i]:
        print("Pivot:", i)
        break
