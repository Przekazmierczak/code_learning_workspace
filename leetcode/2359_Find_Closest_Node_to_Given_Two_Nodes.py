"""
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.
You are also given two integers node1 and node2.
Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.

Example 1:

Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.

Example 2:

Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
"""
from collections import deque

class Solution:
    # def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
    def closestMeetingNode(self, edges, node1, node2):
        que1, que2 = deque([(node1, 0)]), deque([(node2, 0)])
        visit1, visit2 = set(), set()
        res = None
        
        while que1 or que2:
            if que1:
                curr1, distance = que1.popleft()
                if curr1 not in visit1:
                    if curr1 in visit2:
                        if not res:
                            res = (curr1, distance)
                        else:
                            if distance == res[1]:
                                index = min(res[0], curr1)
                                res = (index, distance)
                            else:
                                return res[0]
                    
                    nxt1 = edges[curr1]
                    if nxt1 != -1:
                        que1.append((nxt1, distance + 1))
                    visit1.add(curr1)
            
            if que2:
                curr2, distance = que2.popleft()
                if curr2 not in visit2:
                    if curr2 in visit1:
                        if not res:
                            res = (curr2, distance)
                        else:
                            if distance == res[1]:
                                index = min(res[0], curr2)
                                res = (index, distance)
                            else:
                                return res[0]
                    
                    nxt2 = edges[curr2]
                    if nxt2 != -1:
                        que2.append((nxt2, distance + 1))
                    visit2.add(curr2)
        return res[0] if res else -1
            

def main():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1

    solution = Solution()

    result = solution.closestMeetingNode(edges, node1, node2)
    
    print(result)


if __name__ == "__main__":
    main()