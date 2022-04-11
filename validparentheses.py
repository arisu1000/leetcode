class Solution:
    def isValid(self, s: str) -> bool:

        len_s = len(s)
        is_valid = False

        if len_s % 2 == 1:
            return False

        check = []
        for c in s:
            if c in ("(", "{", "["):
                check.append(c)
            elif c in (")", "}", "]"):
                if len(check) == 0:
                    return False

                tmp = check.pop()
                if c == ")" and tmp == "(":
                    is_valid = True
                elif c == "}" and tmp == "{":
                    is_valid = True
                elif c == "]" and tmp == "[":
                    is_valid = True
                else:
                    return False

        if len(check) > 0:
            is_valid = False

        return is_valid

s = Solution()

print(s.isValid("()"), True)
print(s.isValid("()[]{}"), True)
print(s.isValid("(]"), False)
print(s.isValid("(){}}{"), False)
print(s.isValid("{[]}"), True)
print(s.isValid("([]){"), False)
print(s.isValid("[[[]"), False)