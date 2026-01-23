nums = [1,2,3,4]
n = len(nums)
output = [1] * n
for i in range(1, n):
    output[i] = output[i-1] * nums[i-1]

right = 1
for i in range(n - 1, -1, -1):
    output[i] *= right
    right *= nums[i]

print(output)
