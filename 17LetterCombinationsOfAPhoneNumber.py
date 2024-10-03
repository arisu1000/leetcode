#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description

from typing import List

class Solution:

    lettermap={'2': ['a','b','c'],
               '3': ['d','e','f'],
               '4': ['g','h','i'],
               '5': ['j','k','l'],
               '6': ['m','n','o'],
               '7': ['p','q','r','s'],
               '8': ['t','u','v'],
               '9': ['w','x','y','z']
               }
    
    result = []
    chars = []

    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.chars = []

        for d in digits:
            self.chars.append(self.lettermap[d])

        if len(self.chars) == 0:
            return self.result

        for c in self.chars[0]:
            self.makeLetter(c, 1)

        return self.result

    
    def makeLetter(self, letter, depth):

        if len(self.chars) == depth:
            self.result.append(letter)
            return

        for c in self.chars[depth]:
            self.makeLetter(letter+c, depth+1)





s = Solution()

print(s.letterCombinations("234"), ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])

print(s.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])

print(s.letterCombinations(""), [])
print(s.letterCombinations("2"), ["a","b","c"])