#https://leetcode.com/problems/simplify-path

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')

        ans = []
        for i in range(len(paths)):
            try:
                if paths[i] == ".":
                    continue
                elif paths[i] == "..":
                    ans.pop()
                elif paths[i] == "...":
                    ans.append(paths[i])
                elif paths[i] == "":
                    continue
                else:
                    ans.append(paths[i])
            except IndexError:
                continue

        ans_str = '/'.join(ans)

        return "/"+ans_str[:len(ans_str)]

s = Solution()
print(s.simplifyPath("/home/"), "/home")
print(s.simplifyPath("/home//foo/"), "/home/foo")
print(s.simplifyPath("/home/user/Documents/../Pictures"), "/home/user/Pictures")
print(s.simplifyPath( "/../"), "/")
print(s.simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d")