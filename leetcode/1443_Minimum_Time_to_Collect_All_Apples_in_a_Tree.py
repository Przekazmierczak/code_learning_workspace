"""
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

Example 1:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 2:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0

Constraints:

1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
hasApple.length == n
"""

class Solution:
    # def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    def minTime(self, n, edges, hasApple):
        if not edges:
            return 0
        
        allEdges = {}
        for edge in edges:
            if edge[0] not in allEdges:
                allEdges[edge[0]] = set()
            allEdges[edge[0]].add(edge[1])
            
            if edge[1] not in allEdges:
                allEdges[edge[1]] = set()
            allEdges[edge[1]].add(edge[0])
        
        stack = [[0, None]]
        
        tree = {}
        while stack:
            curr, prev = stack.pop()
            
            if prev != None:
                allEdges[curr].remove(prev)
                tree[curr] = [prev, False]
            for element in allEdges[curr]:
                stack.append([element, curr])

        for i in range(len(hasApple)):
            if hasApple[i]:
                curr = i
                while i != 0 and not tree[i][1]:
                    tree[i][1] = True
                    i = tree[i][0]
        res = 0
        
        for branch in tree.values():
            if branch[1]:
                res += 2
        
        return res
            

def main():
    false = False
    true = True

    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    hasApple = [false,false,true,false,true,true,false]

    solution = Solution()

    result = solution.minTime(n, edges, hasApple)
    
    print(result)


if __name__ == "__main__":
    main()