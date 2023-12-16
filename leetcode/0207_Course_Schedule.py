"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def canFinish(self, numCourses, prerequisites):
        courses = {}
        visited = set()
        
        for i in range(numCourses):
            courses[i] = set()
            
        for course in prerequisites:
            courses[course[0]].add(course[1])
            
        def dfs(course):
            if not courses[course]:
                return True
            if course in visited:
                return False
            
            visited.add(course)
            
            to_remove = []
            for limit in courses[course]:
                if dfs(limit):
                    to_remove.append(limit)
            for course_to_remove in to_remove:
                courses[course].remove(course_to_remove)
                
            if not courses[course]:
                return True
            
            return False
        
        for course in courses:
            dfs(course)
        
        for course in courses:
            if courses[course]:
                return False
        return True
                   
        
    
def main():
    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]

    solution = Solution()

    result = solution.canFinish(numCourses, prerequisites)
    
    print(result)


if __name__ == "__main__":
    main()