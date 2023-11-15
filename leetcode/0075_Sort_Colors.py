"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        last_zero = 0
        
        while left <= right:
            if nums[left] == 0:
                nums[left], nums[last_zero] = nums[last_zero], nums[left]
                left += 1
                last_zero += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        
        return nums
    

def main():
    nums = [2,0,2,1,1,0]

    solution = Solution()

    result = solution.sortColors(nums)
    
    print(result)


if __name__ == "__main__":
    main()