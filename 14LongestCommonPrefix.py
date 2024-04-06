from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        result = ""
        i = 0
        while True:
            currentChar = ""
            countSame = 0
            for str in strs:
                try:
                    if currentChar == "":
                        currentChar = str[i]
                    elif currentChar != str[i]:
                        countSame -= 1
                    
                    countSame += 1
                except KeyError:
                    continue
                except IndexError:
                    continue

            if countSame == length:
                result += currentChar
            else:
                return result

            i += 1

        return result

s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["a"]))

