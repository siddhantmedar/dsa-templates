#Variable size sliding window - Longest substring without repeating character

s = "abcabcbb"
# s = "abacefaabaaaa"

i, j = 0, 0 #ptrs

mp = {}
st = set()
length = 0
start, end = 0, 0

while j< len(s):
    if s[j] not in st:
        st.add(s[j])
        j+=1
    elif s[j] in st:
        if j-i > length:
            length = j-i
            start = i
            end = j-1
        while s[j] in st:
            st.remove(s[i])
            i+=1
        st.add(s[j])
        j+=1

length = max(length, j-i)

print(s[start:end+1])
print(length)
