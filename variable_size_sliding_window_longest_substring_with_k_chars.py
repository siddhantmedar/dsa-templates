#Variable size sliding window

# s = "aabacbebebe"
s = "abacefaabaaaa"
k = 3

i, j = 0, 0 #ptrs

mp = {}
st = set()
length = 0
start, end = 0, 0

while j <= len(s):
    if len(st) < k:
        mp[s[j]] = 1 + mp.get(s[j], 0)
        st.add(s[j])
        j+=1
    if len(st) == k:
        if j-i > length:
            length = (j-i)
            start = i
            end = j-1
        if j < len(s):
            mp[s[j]] = 1+mp.get(s[j], 0)
            st.add(s[j])
        j+=1

    if len(st) > k:
        mp[s[i]]-=1
        if mp[s[i]] == 0:
            st.remove(s[i])
        i+=1

print(s[start: end+1])
print(length)