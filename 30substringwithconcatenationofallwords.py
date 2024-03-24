from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        #words 중에서 하나 매칭되는게 있는지 찾는다.
        #있으면 다음 words중에 매칭되는게 있는지 찾는다.
        #남은 words가 없을때까지 찾는다.
        #남은 words가 0이면 찾았음.
        #매칭되는게 없으면 다음으로 넘어감.

        result = []
        len_words = len(words)
        findindex = -1

        for i in range(0, len_words):

            word = words.pop()
            len_word = len(word)
            findindex = s.find(word)

            right_index = -1
            if findindex >= 0:
                subword = words.pop()
                right_index = s[findindex+len_word:].find(subword)
            
            if right_index == 0:
                result.append(findindex)

        return result
    
    def findStrIndex(l: int, r: int, s: str, word: str) -> int:
        findIndex = s.find(word)
        return findIndex


s = Solution()

print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
