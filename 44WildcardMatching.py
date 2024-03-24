class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = False

        index = 0
        for p_i, p_value in enumerate(p):

            if p_value == '*':
                if p_i == len(p) - 1:
                    return True
                else:

                    while index < len(s) - 1:

                        #index증가시키면서 맞춰봐야함.
                        # 무슨 기준으로 증가시키나??
                        #현재 index와 맞는지 확인
                        # 그 다음 index가 다음 패턴과 맞는지 확인
                        index += 1
                        if p[p_i + 1] == s[index]:
                            break
                        elif p[p_i + 1] == s[index - 1]:
                            index -= 1
                            break
                            
                        

            elif p_value == '?':
                index += 1
            else:
                if p_value == s[index]:
                    index += 1
                    if index >= len(s):
                        if p_i == len(p) -1:
                            return True
                        else:
                            return False
                else:
                    return False


        return result

s = Solution()
print(s.isMatch("aa", "a"), '("aa", "a")')
print(s.isMatch("aa", "*"), '("aa", "*")')
print(s.isMatch("cb", "?a"), '("cb", "?a")')
print(s.isMatch("adceb", "a*b"), '("adceb", "a*b")')
print(s.isMatch("adceb", "*a*b"), '("adceb", "*a*b")')
print(s.isMatch("a", "aa"), '("a", "aa")')