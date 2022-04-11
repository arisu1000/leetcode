from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap = {"2":"abc", 
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz",
                    }

        output = []
        len_digits = len(digits)
        chars = []
        for d in digits:
            chars.append(digitmap[d])
        

        for i in range(0, len(chars)):
            tmp_output = []

            if i == 0:
                for j in range(0, len(chars[i])):    
                    tmp_output.append(chars[i][j])
                output = tmp_output

            else:
                for j in range(0, len(chars[i])):
                    len_output = len(output)
                
                    for o in range(0, len_output):
                        tmp_output.append(output[o] + chars[i][j])
                output = tmp_output

        #멤버를 하나씩 분해해서 자료구조에 넣기
        #자료구조에서 꺼내오면서 조합해서 다시 자료구조에 넣기

        return output

s = Solution()

print(s.letterCombinations("23"))
print(s.letterCombinations("2"))
print(s.letterCombinations(""))

 
