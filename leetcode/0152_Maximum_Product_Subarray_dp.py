"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        result = float("-inf")
        dp = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            curr = nums[i]
            if i > 0:
                prev_max = dp[i - 1][0] * curr
                prev_min = dp[i - 1][1] * curr

                num_max = max(curr, prev_max, prev_min)
                num_min = min(curr, prev_max, prev_min)
                
                dp[i] = (num_max, num_min)
                result = max(result, num_max)
            else:
                dp[i] = (curr, curr)
                result = max(curr, curr)

        return result

def main():
    nums = [2,-5,-2,-4,3]

    solution = Solution()

    result = solution.maxProduct(nums)
    
    print(result)


if __name__ == "__main__":
    main()