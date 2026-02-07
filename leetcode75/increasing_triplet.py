## nums = [1,2,3,4,5]
## True
## [5,4,3,2,1]
## flase

nums = [2,1,5,0,4,6]
"""
first = float('inf')
second = float('inf')
for num in nums:
    if num <= first:
        first = num
    elif num <= second:
        second = num
    else:
        print(True)
        break
else:
    print(False)
"""

first = float('-inf')
second = float('-inf')

for num in nums:
    if num >= first:
        first = num
    elif num >= second:
        second = num
    else:
        print(True)
        break
else:
    print(False)
