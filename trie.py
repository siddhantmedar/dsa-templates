class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.mp = {}
        self.isEnd = False

class Trie:
    root = Node('/')
    
    def insert(self, word):
        tmpRoot = self.root

        for c in word:
            if c not in tmpRoot.mp:
                charNode = Node(c)
                tmpRoot.mp[c] = charNode
            tmpRoot = tmpRoot.mp[c]
        tmpRoot.isEnd = True
        return
    
    def search(self, word):
        tmpRoot = self.root

        for c in word:
            if c not in tmpRoot.mp:
                return False
            tmpRoot = tmpRoot.mp[c]

        return tmpRoot.isEnd

rt = Trie()
rt.insert("apple")
print(rt.search("apple"))
print(rt.search("apple"))