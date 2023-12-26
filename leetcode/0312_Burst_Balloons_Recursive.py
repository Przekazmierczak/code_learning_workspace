"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    def maxCoins(self, nums):
        memo = {}
        nums = [1] + nums + [1]
        result = [0]

        def burst(start, end):
            if start > end:
                return 0
            
            if (start, end) in memo:
                return memo[(start, end)]
            
            max_value = 0
            for balloon in range(start, end + 1):
                max_value = max(max_value, burst(start, balloon - 1) + nums[start - 1] * nums[balloon] * nums[end + 1] + burst(balloon + 1, end))

            result[0] = max(result[0], max_value)
            memo[start, end] = max_value

            return max_value
        
        burst(1, len(nums) - 2)

        return result[0]



def main():
    nums = [3,1,5,8]

    solution = Solution()

    result = solution.maxCoins(nums)
    
    print(result)


if __name__ == "__main__":
    main()