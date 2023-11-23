"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        ans = [1] * (len(nums))
        
        current_val = 1
        for i in range(1, len(nums)):
            current_val *= nums[i - 1]
            ans[i] = current_val

        current_val = 1
        for i in reversed(range(len(nums) - 1)):
            current_val *= nums[i + 1]
            ans[i] *= current_val
        
        return ans


def main():
    nums = [1,2,3,4]

    solution = Solution()

    result = solution.productExceptSelf(nums)
    
    print(result)


if __name__ == "__main__":
    main()