from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        n = len(strs)
        
        store = {}
        for i in range(n):
            try:
                store[''.join(sorted(strs[i]))].append(i)
            except KeyError:
                store[''.join(sorted(strs[i]))] = [i]
        
        # print(store)
        result = []
        for key, value in store.items():
            tmp_result = []
            for i in value:
                tmp_result.append(strs[i])
            
            result.append(tmp_result)

        return result



s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))