"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4
 
Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    def largestRectangleArea(self, heights):
        def largest(heights, left, right):
            if left > right:
                return 0
            
            min_index = left
            for i in range(left, right + 1):
                if heights[i] < heights[min_index]:
                    min_index = i

            current_area = (right - left + 1) * heights[min_index]

            return max(current_area, largest(heights, left, min_index - 1), largest(heights, min_index + 1, right))

        max_area = largest(heights, 0, len(heights) - 1)

        return max_area
    
def main():
    heights = [1,1,1]

    solution = Solution()

    result = solution.largestRectangleArea(heights)
    
    print(result)


if __name__ == "__main__":
    main()