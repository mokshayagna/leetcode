s = "IceCreAm"
##"AceCreIm"
left = 0
print(len(s))
right = len(s)-1
a = list(s)
res = ""
vowels= "AEIOUaeiou"
while left < right:
    if a[left] not in vowels:
        left += 1
    if a[right] not in vowels:
        right -= 1
    else:
        a[left],a[right] = a[right],a[left]
        left += 1
        right -= 1
    res = "".join(a)
print(res)
