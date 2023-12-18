"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
# from collections import deque
import heapq

class Solution:
    # def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    def networkDelayTime(self, times, n, k):
        graph = {}
        visit = set()
        res = 0

        for time in times:
            node1, node2, distance = time
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append((distance, node2))

        heap = [(0, k)]
        heapq.heapify(heap)

        while len(visit) < n and heap:
            dist, node = heap[0]
            heapq.heappop(heap)
            if node not in visit:
                visit.add(node)
                res = dist
                for neigh in graph[node]:
                    curr_dist, curr_neigh = neigh
                    if curr_neigh not in visit:
                        heapq.heappush(heap, (curr_dist + res, curr_neigh))
        
        if len(visit) == n:
            return res
        return -1


    
def main():
    times = [[1,2,1]]
    n = 2
    k = 2
    solution = Solution()

    result = solution.networkDelayTime(times, n, k)
    
    print(result)


if __name__ == "__main__":
    main()