"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""

class Solution:
    # def arraySign(self, nums: List[int]) -> int:
    def arraySign(self, nums):
        res = 1
        for num in nums:
            if num < 0:
                res *= -1
            elif num == 0:
                res = 0
                break
        return res
            

def main():
    nums = [1,5,0,2,-3]

    solution = Solution()

    result = solution.arraySign(nums)
    
    print(result)


if __name__ == "__main__":
    main()
