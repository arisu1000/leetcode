#https://leetcode.com/problems/design-add-and-search-words-data-structure


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word: str) -> bool:
        return self._search_recursive(word, 0, self.root)
    
    def _search_recursive(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end_of_word
        
        char = word[index]

        if char == '.':
            for child in node.children.values():
                if self._search_recursive(word, index + 1, child):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self._search_recursive(word, index + 1, node.children[char])
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

s = WordDictionary()

s.addWord("bad")
s.addWord("dad")
s.addWord("mad")

print(s.search("pad"), False)
print(s.search("bad"), True)
print(s.search(".ad"), True)
print(s.search("b.."), True)

s = WordDictionary()
s.addWord("at")
s.addWord("and")
s.addWord("an")
s.addWord("add")

print(s.search("a"), False)