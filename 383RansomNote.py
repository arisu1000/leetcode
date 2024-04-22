#https://leetcode.com/problems/ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = False

        list = []
        for i in range(len(ransomNote)):
            isFind = False
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j]:
                    if j in list:
                        continue

                    isFind = True
                    list.append(j)
                    break

            if isFind == False:
                return ans
            
        if len(list) == len(ransomNote):
            ans = True    
        
        return ans

s = Solution()
print(s.canConstruct("a", "b"), False)
print(s.canConstruct("aa", "ab"), False)
print(s.canConstruct("aa", "aab"), True)