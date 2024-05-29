"""
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.
A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:

Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:

Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
"""

class Solution:
    # def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    def largestPathValue(self, colors, edges):
        colorsArray = [None for _ in range(len(colors))]
        dic = [[] for _ in range(len(colors))]
        for edge in edges:
            dic[edge[0]].append(edge[1])
        
        def combine(prevs):
            curr = {}
            max_ = 0
            circle = False
            for prev in prevs:
                max_= max(prev[1], max_)
                circle = prev[2] or circle
                for element in prev[0]:
                    if element in curr:
                        curr[element] = max(curr[element], prev[0][element])
                    else:
                        curr[element] = prev[0][element]
            return [curr, max_, circle]
        
        
        def dfs(node):
            if node in visit:
                return [{}, 0, True]
            
            if colorsArray[node]:
                return colorsArray[node]
            visit.add(node)

            if not dic[node]:
                res = [{colors[node]: 1}, 1, False]
                colorsArray[node] = res
                visit.remove(node)
                return res
            
            curr = []
            for nxt in dic[node]:
                curr.append(dfs(nxt))
            res = combine(curr)

            if colors[node] in res[0]:
                res[0][colors[node]] += 1
                res[1] = max(res[1], res[0][colors[node]])    
            else:
                res[0][colors[node]] = 1

            colorsArray[node] = res
            visit.remove(node)
            return res
        
        ans = 0
        visit = set()
        for node in range(len(colors)):
            if not colorsArray[node]:
                _, max_, has_circle = dfs(node)
                if has_circle:
                    return -1
                ans = max(max_, ans)
        return ans
            

def main():
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]

    solution = Solution()

    result = solution.largestPathValue(colors, edges)
    
    print(result)


if __name__ == "__main__":
    main()