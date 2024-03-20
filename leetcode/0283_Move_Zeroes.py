"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums
            

def main():
    nums = [0,1,0,3,12]

    solution = Solution()

    result = solution.moveZeroes(nums)
    
    print(result)


if __name__ == "__main__":
    main()