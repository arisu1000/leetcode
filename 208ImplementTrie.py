
#https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    elements = []

    def __init__(self):
        self.elements = []
        return

    def insert(self, word: str) -> None:
        self.elements.append(word)
        return
        

    def search(self, word: str) -> bool:
        try:
            self.elements.index(word)
            return True
        except ValueError:
            return False        

    def startsWith(self, prefix: str) -> bool:
        for e in self.elements:
            if e.startswith(prefix):
                return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

s = Trie()
s.insert("apple")
print(s.search("apple"), True)
print(s.search("app"), False)
print(s.startsWith("app"), True)
s.insert("app")
print(s.search("app"), True)
