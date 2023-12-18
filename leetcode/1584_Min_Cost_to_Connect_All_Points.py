"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
import heapq

class Solution:
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    def minCostConnectPoints(self, points):
        cost = 0
        num_points = len(points)
        visit = set()
        heap = []
        heapq.heapify(heap)

        def distance(point1, point2):
            x1, y1 = points[point1]
            x2, y2 = points[point2]
            return abs(x1 - x2) + abs(y1 - y2)
        
        heapq.heappush(heap, (0,0))
        while len(visit) < num_points:
            dist, point = heap[0]
            heapq.heappop(heap)

            if point not in visit:
                cost += dist
                visit.add(point)
                for index in range(num_points):
                    if index not in visit:
                        heapq.heappush(heap, (distance(point, index), index))

        return cost

    
def main():
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()

    result = solution.minCostConnectPoints(points)
    
    print(result)


if __name__ == "__main__":
    main()