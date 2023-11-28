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
        stack, ans, i = [], 0, 0
        
        while i < len(heights) or stack:
            if i < len(heights) and (not stack or heights[i] > heights[stack[-1]]):
                stack.append(i)
                i += 1
            
            else:
                height = stack.pop()
                if stack:
                    area = heights[height] * (i -1 - stack[-1])
                else:
                    area = heights[height] * i
                ans = max(ans, area)
        
        return ans
    
def main():
    heights = [2,2,1,5,6]

    solution = Solution()

    result = solution.largestRectangleArea(heights)
    
    print(result)


if __name__ == "__main__":
    main()