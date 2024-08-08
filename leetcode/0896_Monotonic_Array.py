"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""

class Solution:
    # def isMonotonic(self, nums: List[int]) -> bool:
    def isMonotonic(self, nums):
        state = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if not state:
                    state = -1
                elif state == 1:
                    return False
            elif nums[i - 1] < nums[i]:
                if not state:
                    state = 1
                elif state == -1:
                    return False
        
        return True
            

def main():
    nums = [6,5,4,4]

    solution = Solution()

    result = solution.isMonotonic(nums)
    
    print(result)


if __name__ == "__main__":
    main()