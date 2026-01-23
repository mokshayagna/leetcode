nums = [1,8,6,2,5,4,8,3,7,9]
# Output: 49
i = 0
j = len(nums)
max_val = nums[0]

while i < j:
    if nums[i] > max_val:
        max_val = nums[i]
        max_index = j - i
    i += 1

print(max_val)
print(max_index)