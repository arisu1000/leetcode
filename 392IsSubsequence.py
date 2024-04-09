# https://leetcode.com/problems/is-subsequence


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        match_count = 0
        len_s = len(s)
        if len_s == 0:
            return True

        while s_index < len_s and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
                match_count += 1
                if match_count == len_s:
                    return True
            else:
                t_index += 1

        return False


s = Solution()
print(s.isSubsequence("abc", "ahbgdc"), True)
print(s.isSubsequence("axc", "ahbgdc"), False)
print(s.isSubsequence("", "ahbgdc"), True)
