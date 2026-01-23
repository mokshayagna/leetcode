s = "the sky is blue"
words = []
for i in s.split():
    words.append(i)
print(words)
res = ""
i = 0
j = len(words) -1
while i < j:
    words[j],words[i] = words[i],words[j]
    i += 1
    j -= 1
res = " ".join(words)
print(res)
