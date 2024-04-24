#https://leetcode.com/problems/valid-anagram

# timeout은 아닌데 시간이 오래 걸림
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         len_s = len(s)
#         if len_s != len(t):
#             return False
        
#         sorted_s = sorted(s)
#         sorted_t = sorted(t)

#         for i in range(len_s):
#             if sorted_s != sorted_t:
#                 return False
            
#         return True

# 위에꺼 보단 빠르지만 여전히 느리다.
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         len_s = len(s)
#         if len_s != len(t):
#             return False
        
#         for i in range(len_s):
#             t = t.replace(s[i], '', 1)

#         if len(t) == 0:
#             return True
#         else:
#             return False

# 두번째꺼보다 느림        
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         len_s = len(s)
#         if len_s != len(t):
#             return False
        
#         list_t = list(t)

#         for i in range(len_s):
#             try:
#                 list_t.remove(s[i])
#             except ValueError:
#                 return False
                
#         if len(list_t) == 0:
#             return True
#         else:
#             return False
     
s = Solution()
print(s.isAnagram("anagram", "nagaram"), True)        
print(s.isAnagram("rat", "cat"), False)        