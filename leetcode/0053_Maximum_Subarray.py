"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        left, right, max_sum, current_sum = 0, 0, float("-inf"), 0
        
        while left < len(nums):
            if right < len(nums) and (left == right or current_sum >= 0):
                current_sum += nums[right]
                right += 1
                
            else:
                current_sum -= nums[left]
                left += 1
                
            if right > left:
                max_sum = max(current_sum, max_sum)
        return max_sum


def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]

    solution = Solution()

    result = solution.maxSubArray(nums)
    
    print(result)


if __name__ == "__main__":
    main()