def groupOfStrings(words):
    def dfs(bitmask):
        if bitmask not in mp:
            return 0
        size = mp[bitmask]
        del mp[bitmask]

        for i in range(26):
            newbitmask = bitmask ^ (1 << i)
            size += dfs(newbitmask)

        for i in range(26):
            if (bitmask & (1 << i)) > 0:
                for j in range(26):
                    if (bitmask & (1 << j)) == 0:
                        newbitmask = bitmask ^ (1 << i)
                        newbitmask = newbitmask ^ (1 << j)
                        size += dfs(newbitmask)

        return size

    mp = {}
    for word in words:
        bitmask = 0
        for char in word:
            bitmask |= (1 << (ord(char) - ord('a')))
        mp[bitmask] = 1 + mp.get(bitmask, 0)

    # print(mp)
    groups, maxsize = 0, -1

    unique = list(set(mp.keys()))

    for k in unique:
        if k in mp:
            groups += 1
            size = dfs(k)
            maxsize = max(maxsize, size)

    return [groups, maxsize]


# words = ["a","b","ab","cde"]
words = ["a","ab","abc"]
print(groupOfStrings(words))