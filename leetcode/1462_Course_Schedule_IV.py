"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.
For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.
You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.
Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:

Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Constraints:

2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi <= n - 1
ui != vi
"""

class Solution:
    # def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        req = [set() for _ in range(numCourses)]
        for pre in prerequisites:
            req[pre[1]].add(pre[0])
        
        def findPre(node):
            if visit[node]:
                return req[node]
            req_list = list(req[node])
            for curr in req_list:
                req[node].update(findPre(curr))
            visit[node] = True
            return req[node]
                
        
        visit = [False] * numCourses
        for node in range(numCourses):
            if not visit[node]:
                req[node].update(findPre(node))
        
        res = []
        for querie in queries:
            if querie[0] in req[querie[1]]:
                res.append(True)
            else:
                res.append(False)
        return res
            

def main():
    numCourses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1,0],[1,2]]

    solution = Solution()

    result = solution.checkIfPrerequisite(numCourses, prerequisites, queries)
    
    print(result)


if __name__ == "__main__":
    main()