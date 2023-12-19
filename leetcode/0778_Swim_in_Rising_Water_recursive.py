"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example 1:

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
"""
import heapq

class Solution:
    # def swimInWater(self, grid: List[List[int]]) -> int:
    def swimInWater(self, grid):
        n = len(grid)
        heap = []
        visit = set()
        heapq.heapify(heap)

        def swim(row, column, time):
            if row == n - 1 and column == n - 1:
                return time
            
            if (row, column) not in visit:
                visit.add((row, column))
                if row < n - 1:
                    heapq.heappush(heap, (max(time, grid[row + 1][column]), row + 1, column))
                if row > 0:
                    heapq.heappush(heap, (max(time, grid[row - 1][column]), row - 1, column))
                if column < n - 1:
                    heapq.heappush(heap, (max(time, grid[row][column + 1]), row, column + 1))
                if column > 0:
                    heapq.heappush(heap, (max(time, grid[row][column - 1]), row, column - 1))

            new_time, new_row, new_column = heap[0]
            heapq.heappop(heap)

            return swim(new_row, new_column, new_time)
        
        return swim(0, 0, grid[0][0])

    
def main():
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    solution = Solution()

    result = solution.swimInWater(grid)
    
    print(result)


if __name__ == "__main__":
    main()