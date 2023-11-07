"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    # def trap(self, height: List[int]) -> int:
    def trap(self, height):
        current_left_index = 0
        max_left_value = 0
        current_right_index = len(height) - 1
        max_right_value = height[len(height) - 1]

        ans = 0

        while current_left_index <= current_right_index:
            if max_left_value <= max_right_value:
                amount = max_left_value - height[current_left_index]
                if amount > 0:
                    ans += amount
                max_left_value = max(max_left_value, height[current_left_index])
                current_left_index += 1
            else:
                amount = max_right_value - height[current_right_index]
                if amount > 0:
                    ans += amount
                max_right_value = max(max_right_value, height[current_right_index])
                current_right_index -= 1
        
        return ans

def main():
    height = [4,2,3]

    solution = Solution()

    result = solution.trap(height)
    
    print(result)


if __name__ == "__main__":
    main()