"""
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.
For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.
Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
"""

class Solution:
    # def maxSumMinProduct(self, nums: List[int]) -> int:
    def maxSumMinProduct(self, nums):
        SUM = sum(nums)
        curr_left = 0
        curr_right = SUM
        left = [0]
        right = [SUM]
        for i in range(len(nums)):
            curr_left += nums[i]
            curr_right -= nums[i]
            left.append(curr_left)
            right.append(curr_right)
        
        stack = []
        res = 0
        
        for i in range(len(nums)):
            start = 0
            if not stack:
                stack.append((nums[i], start))
            elif stack[-1][0] <= nums[i]:
                start = i
                stack.append((nums[i], start))
            else:
                while stack and stack[-1][0] >= nums[i]:
                    if stack:
                        value, start = stack.pop()
                        res = max(value * (SUM - left[start] - right[i]), res)
                stack.append((nums[i], start))
        
        i += 1
        
        while stack:
            value, start = stack.pop()
            res = max(value * (SUM - left[start] - right[i]), res)
        return res % (10 ** 9 + 7)
            

def main():
    nums = [2,3,3,1,2]

    solution = Solution()

    result = solution.maxSumMinProduct(nums)
    
    print(result)


if __name__ == "__main__":
    main()