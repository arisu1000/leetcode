#https://leetcode.com/problems/evaluate-division

from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        #방정식을 풀어서 나눗셈을 해결해야 하나?
        known_variables=set()
        calculated = {}
        for i, equation in enumerate(equations):
            for var in equation:
                for c in var:
                    known_variables.add(c)
            
            calculated[f"{equation[0]}/{equation[1]}"] = values[i]
        

        ans = []
        for query in queries:
            unknown_variable = False
            for var in query:
                for c in var:
                    if c not in known_variables:
                        unknown_variable = True
            
            if unknown_variable:
                ans.append(-1.0)
                continue
            
            if query[0] == query[1]:
                ans.append(1.0)
                continue
            
            equation = f"{query[0]}/{query[1]}"

            try:
                if calculated[equation]:
                    ans.append(calculated[equation])
                    continue
            except KeyError:
                first = ""
                second = ""
                    


            ans.append(1.0)
                



        return ans
    
s = Solution()


print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.0, 0.5, -1.0, 1.0, -1.0 ])

print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), [3.75000,0.40000,5.00000,0.20000])

print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]), [0.50000,2.00000,-1.00000,-1.00000])