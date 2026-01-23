flowerbed = [1, 0, 0, 0, 1]
n = 2
b = len(flowerbed)

for i in range(b):
    if flowerbed[i] == 0:
        if i == 0:
            if flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        elif i == b-1:
            if flowerbed[i-1] == 0:
                flowerbed[i] = 1
                n -= 1

        else:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

    if n == 0:
        break

print(flowerbed)
print(n == 0)



