#https://leetcode.com/problems/text-justification

from typing import List
import math

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        line_words_length = 0
        rowIndex = [] 
        while i < len(words):
            if len(words[i]) + line_words_length <= maxWidth:
                rowIndex.append(i)
                line_words_length += len(words[i]) + 1
                i += 1
            else:
                row = ""
                wordsLength = 0
                for k in rowIndex:
                    wordsLength += len(words[k])
                
                padding = maxWidth
                padding_count = len(rowIndex) - 1
                if len(rowIndex) > 1:
                    padding = math.floor((maxWidth - wordsLength) / padding_count)

                residueEmptyString = 0
                if padding_count != 0:
                    residueEmptyString = ((maxWidth - wordsLength) % padding_count)
                    
                for k in rowIndex:
                    row += words[k] + (" " * padding)

                    if residueEmptyString > 0:
                        row += " "
                        residueEmptyString -= 1

                row = row[0:maxWidth]

                ans.append(row)

                rowIndex = []
                line_words_length = 0
            
        row = ""
        
        for k in rowIndex:
            row += words[k] + " "

        lastPadding = " " * (maxWidth - len(row))
        row += lastPadding

        row = row[0:maxWidth]

        ans.append(row)

        return ans
    


s = Solution()
print(s.fullJustify( ["This", "is", "an", "example", "of", "text", "justification."], 16))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))
print(s.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"],16))