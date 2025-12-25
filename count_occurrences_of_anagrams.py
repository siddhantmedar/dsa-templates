# Count Occurrences Of Anagrams | Sliding Window

s = "forxxorfxdofr"
p = "for"
k = len(p)

mp = {}

for c in p:
    mp[c] = 1 + mp.get(c,0)

dist_count = len(set(p))
res = 0

for i in range(k):
    if s[i] in mp:
        mp[s[i]]-=1
        if mp[s[i]] == 0:
            dist_count -=1

if dist_count == 0:
    res+=1

for i in range(k, len(s)):
    if s[i-k] in mp:
        mp[s[i-k]]+=1
        if mp[s[i-k]] == 1:
            dist_count+=1
    #current element
    if s[i] in mp:
        mp[s[i]]-=1
        if mp[s[i]] == 0:
            dist_count-=1
    if dist_count == 0:
        res+=1

print(res)
