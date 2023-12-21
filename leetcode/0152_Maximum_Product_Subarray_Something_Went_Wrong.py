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
        curr_max = float("-inf")
        curr_max_neg = float("-inf")

        for num in nums:
            if num > 0:
                curr_max = curr_max * num if curr_max != float("-inf") else num
                curr_max_neg = curr_max_neg * num if curr_max_neg != float("-inf") else num

            elif num < 0:
                curr_max_neg = curr_max_neg * num if curr_max_neg != float("-inf") else num
                if curr_max_neg > 0:
                    curr_max = curr_max_neg
                else:
                    curr_max = float("-inf")

            else:
                curr_max = float("-inf")
                curr_max_neg = float("-inf")
                result = max(result, 0)

            result = max(result, curr_max, curr_max_neg)

        curr_max = float("-inf")
        curr_max_neg = float("-inf")

        for num in reversed(nums):
            if num > 0:
                curr_max = curr_max * num if curr_max != float("-inf") else num
                curr_max_neg = curr_max_neg * num if curr_max_neg != float("-inf") else num

            elif num < 0:
                curr_max_neg = curr_max_neg * num if curr_max_neg != float("-inf") else num
                if curr_max_neg > 0:
                    curr_max = curr_max_neg
                else:
                    curr_max = float("-inf")

            else:
                curr_max = float("-inf")
                curr_max_neg = float("-inf")
                result = max(result, 0)

            result = max(result, curr_max, curr_max_neg)
        
        return result

def main():
    nums = [2,-5,-2,-4,3]

    solution = Solution()

    result = solution.maxProduct(nums)
    
    print(result)


if __name__ == "__main__":
    main()