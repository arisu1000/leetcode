#https://leetcode.com/problems/design-add-and-search-words-data-structure

import re

class WordDictionary:

    dictionary = []

    def __init__(self):
        self.dictionary = []

    def addWord(self, word: str) -> None:
        self.dictionary.append(word)
        
    def search(self, word: str) -> bool:
        for entry in self.dictionary:
            if re.match(word+'$', entry):
                return True

        return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

s = WordDictionary()

# s.addWord("bad")
# s.addWord("dad")
# s.addWord("mad")

# print(s.search("pad"), False)
# print(s.search("bad"), True)
# print(s.search(".ad"), True)
# print(s.search("b.."), True)

s.addWord("at")
s.addWord("and")
s.addWord("an")
s.addWord("add")

print(s.search("a"), False)