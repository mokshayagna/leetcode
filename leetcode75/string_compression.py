chars = ["a","a","b","b","c","c","c"]

q = []
i = 0

while i < len(chars):
    count = 1
    
    while i + 1 < len(chars) and chars[i] == chars[i+1]:
        count += 1
        i += 1
    
    q.append(chars[i])
    
    if count > 1:
        q.append(str(count))
    
    i += 1

print(q)
