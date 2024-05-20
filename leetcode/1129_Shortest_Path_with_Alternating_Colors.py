"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.
You are given two arrays redEdges and blueEdges where:
redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
from collections import deque

class Solution:
    # def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        nodesRed = [set() for _ in range(n)]
        nodesBlue = [set() for _ in range(n)]
        
        for edge in redEdges:
            nodesRed[edge[0]].add(edge[1])
        for edge in blueEdges:
            nodesBlue[edge[0]].add(edge[1])
        
        visitRed = {0: 0}
        visitBlue = {}
        que = deque([(0, "blue", 0), (0, "red", 0)])
        
        while que:
            i, prev, steps = que.popleft()
            if prev == "blue":
                for node in nodesRed[i]:
                    if node not in visitBlue:
                        visitBlue[node] = steps + 1
                        que.append((node, "red", steps + 1))
            else:
                for node in nodesBlue[i]:
                    if node not in visitRed:
                        visitRed[node] = steps + 1
                        que.append((node, "blue", steps + 1))
        res = []
        for i in range(n):
            if i in visitBlue and i not in visitRed:
                res.append(visitBlue[i])
            elif i in visitRed and i not in visitBlue:
                res.append(visitRed[i])
            elif i in visitBlue and i in visitRed:
                res.append(min(visitBlue[i], visitRed[i]))
            else:
                res.append(-1)
        return res
            

def main():
    n = 3
    redEdges = [[0,1]]
    blueEdges = [[2,1]]

    solution = Solution()

    result = solution.shortestAlternatingPaths(n, redEdges, blueEdges)
    
    print(result)


if __name__ == "__main__":
    main()