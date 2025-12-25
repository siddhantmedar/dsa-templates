order = "cba"
str = "abbcd"
# Output: "cbad"

res = []
count = [0]*26

for c in str:
    count[ord(c) - ord('a')]+=1

for c in order:
    while count[ord(c)-ord('a')] > 0:
        res.append(c)
        count[ord(c)-ord('a')]-=1

for i in range(len(count)):
    while count[i] > 0:
        res.append(chr(97+i))
        count[i]-=1
        
print("".join(res))