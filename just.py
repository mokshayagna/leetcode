s = "IceCreAm"
##"AceCreIm"##
a = list(s)
left = 0
right = len(a) -1
vowels = "aeiouAEIOU"
while left<right:
    if a[left] not in vowels:
        left += 1
    elif a[right] not in vowels:
        right -= 1
    else:
        a[right],a[left] = a[left],a[right]
        left += 1
        right -= 1
res = "".join(a)
print(res)
        