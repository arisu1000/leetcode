# https://leetcode.com/problems/word-break

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # 빈 문자열은 항상 나뉠 수 있음

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
        
            

        
        
        


s = Solution()
print(s.wordBreak("catsandogcat",["cats","dog","sand","and","cat","an"] ), True)
print(s.wordBreak("cars",["car","ca","rs"] ), True)
print(s.wordBreak("bb",["a","b","bbb","bbbb"] ), True)
print(s.wordBreak("leetcode", ["leet","code"]), True)
print(s.wordBreak("applepenapple", ["apple","pen"]), True)
print(s.wordBreak("catsandog",["cats","dog","sand","and","cat"] ), False)
