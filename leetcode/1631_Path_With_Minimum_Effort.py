"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:

Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""
import heapq

class Solution:
    # def minimumEffortPath(self, heights: List[List[int]]) -> int:
    def minimumEffortPath(self, heights):
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        
        res = 0

        ROWS, COLS = len(heights), len(heights[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit = {}
        visit[(0, 0)] = 0

        while True:
            effort, row, col = heapq.heappop(heap)
            res = max(effort, res)

            if row == ROWS - 1 and col == COLS - 1:
                return res

            for neighbor in neighbors:
                neigh_row, neigh_col = neighbor
                new_row = neigh_row + row
                new_col = neigh_col + col

                if new_row in range(ROWS) and new_col in range(COLS):
                    new_effort = abs(heights[row][col] - heights[new_row][new_col])
                    if (new_row, new_col) not in visit or visit[(new_row, new_col)] > new_effort:
                        visit[(new_row, new_col)] = new_effort
                        heapq.heappush(heap, (new_effort, new_row, new_col))
            

def main():
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

    solution = Solution()

    result = solution.minimumEffortPath(heights)
    
    print(result)


if __name__ == "__main__":
    main()