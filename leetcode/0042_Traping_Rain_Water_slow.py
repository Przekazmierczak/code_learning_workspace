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
        def water_amount(left, right, terrain):
            smaller = min(terrain[left][0], terrain[right][0])
            amount = 0
            for index in range(left +1, right):
                amount += smaller - terrain[index][0]
            return amount

        def find_peaks(left, right, terrain):
            new_terrain = sorted(terrain[left:right + 1])
            first_max = new_terrain[-1][1]
            second_max = new_terrain[-2][1]
            left = min(first_max, second_max)
            right = max(first_max, second_max)
            return (left, right)

        def solution(left, right, terrain):
            if right - left <= 1:
                return 0
            new_left, new_right = find_peaks(left, right, terrain)
            return solution(left, new_left, terrain) + solution(new_right, right, terrain) + water_amount(new_left, new_right, terrain)
        
        for index in range(len(height)):
            height[index] = (height[index], index)
            
        return solution(0, len(height), height)




def main():
    height = [4,2,0,3,2,5]

    solution = Solution()

    result = solution.trap(height)
    
    print(result)


if __name__ == "__main__":
    main()