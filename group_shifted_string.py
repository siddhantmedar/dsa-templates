def findKey(s):
    key=""
    for i in range(1, len(s)):
        curr = s[i]
        prev = s[i - 1]
        diff = ord(curr) - ord(prev)
        if diff < 0:
            diff += 26
        key +=(str(diff)+"#")
    key += "."
    return key


def groupShiftedStrings(lst):
    mp = {}
    for word in lst:
        k = findKey(word)
        if k in mp:
            mp[k].append(word)
        else:
            mp[k] = [word]
    return [v for _, v in mp.items()]


lst = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(groupShiftedStrings(lst))