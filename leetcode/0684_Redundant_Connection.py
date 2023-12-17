"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

class Solution:
    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(1, n + 1)]
        number_of_connections = [1 for _ in range(len(edges))]

        for edge in edges:
            parent1, parent2 = edge

            while parent[parent1 - 1] != parent1:
                parent1 = parent[parent1 - 1]

            while parent[parent2 - 1] != parent2:
                parent2 = parent[parent2 - 1]

            if parent1 == parent2:
                return edge

            if number_of_connections[parent1 - 1] >= number_of_connections[parent2 - 1]:
                number_of_connections[parent1 - 1] += 1
                parent[parent2 - 1] = parent1
            else:
                number_of_connections[parent2 - 1] += 1
                parent[parent1 - 1] = parent2
        

def main():
    edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]

    solution = Solution()

    result = solution.findRedundantConnection(edges)
    
    print(result)


if __name__ == "__main__":
    main()