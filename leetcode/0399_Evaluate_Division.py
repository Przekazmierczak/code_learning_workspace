"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

class Solution:
    # def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    def calcEquation(self, equations, values, queries):
        div = {}
        multi = {}
        val = {}
        visit = set()
        
        for i in range(len(equations)):
            if equations[i][0] not in div:
                div[equations[i][0]] = []
            div[equations[i][0]].append((equations[i][1], values[i]))
            
            if equations[i][1] not in multi:
                multi[equations[i][1]] = []
            multi[equations[i][1]].append((equations[i][0], values[i]))
        
        def dfs(node, i):
            visit.add(node)
            if node not in val:
                val[node] = (1.0, i)
            if node in div:
                for num in div[node]:
                    val[num[0]] = (val[node][0] / num[1], i)
                    if num[0] not in visit:
                        dfs(num[0], i)
            if node in multi:
                for num in multi[node]:
                    val[num[0]] = (val[node][0] * num[1], i)
                    if num[0] not in visit:
                        dfs(num[0], i)
        i = 0
        for num in div:
            if num not in val:
                dfs(num, i)
                i += 1
        
        res = []
        for querie in queries:
            if querie[0] in val and querie[1] in val and val[querie[0]][1] == val[querie[1]][1]:
                res.append(val[querie[0]][0] / val[querie[1]][0])
            else:
                res.append(-1)
            
        return res
            

def main():
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    solution = Solution()

    result = solution.calcEquation(equations, values, queries)
    
    print(result)


if __name__ == "__main__":
    main()