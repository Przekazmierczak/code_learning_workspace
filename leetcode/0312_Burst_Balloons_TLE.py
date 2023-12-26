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
        def burst(baloons):
            if not baloons:
                return 0
            
            if tuple(baloons) in memo:
                return memo[tuple(baloons)]

            max_amount = 0
            for i in range(len(baloons)):
                if i > 0:
                    neighbor1 = baloons[i - 1]
                else:
                    neighbor1 = 1

                if i < len(baloons) - 1:
                    neighbor2 = baloons[i + 1]
                else:
                    neighbor2 = 1

                amount = neighbor1 * baloons[i] * neighbor2 + burst(baloons[:i] + baloons[i + 1:])
                max_amount = max(max_amount, amount)
            
            memo[tuple(baloons)] = max_amount

            return max_amount
        
        return burst(nums)


def main():
    nums = [3,1,5,8,10,9,33,23,12,1,3,2,4,2]

    solution = Solution()

    result = solution.maxCoins(nums)
    
    print(result)


if __name__ == "__main__":
    main()