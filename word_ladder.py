from collections import deque
import copy


def wordLadder(lst, startword, endword):
    def findNeighbours(word):
        words = list(word)
        for i in range(len(words)):
            wordscpy = copy.deepcopy(words)
            for j in range(97, 123):
                wordscpy[i] = chr(j)
                candidate = "".join(wordscpy)
                if candidate in mp and not mp[candidate]:
                    q.append(candidate)
                    mp[candidate] = True

    if endword not in lst:
        return 0

    mp = {}

    for word in lst:
        mp[word] = False

    q = deque()
    count = 1
    q.append(startword)
    mp[startword] = True

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endword:
                return count
            findNeighbours(word)
        count += 1

    return 0


lst = ["hot", "dot", "dog", "lot", "log", "cog"]
# lst = ["hot","dot","dog","lot","log"]
print(wordLadder(lst, "hit", "cog"))
