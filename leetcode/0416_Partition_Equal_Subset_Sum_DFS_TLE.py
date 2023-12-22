"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        goal = nums_sum // 2
        memo = {}
        
        def dfs(remaining_sum, remaining_list):
            if remaining_sum < 0:
                return False
            
            if remaining_sum == 0:
                return True
            
            if (remaining_sum, tuple(remaining_list)) in memo:
                return memo[(remaining_sum, tuple(remaining_list))]

            for num in remaining_list:
                next_list = remaining_list.copy()
                next_list.remove(num)
                if dfs(remaining_sum - num, next_list):
                    memo[(remaining_sum, tuple(remaining_list))] = True
                    return True
                
            memo[(remaining_sum, tuple(remaining_list))] = False
            return False

        return dfs(goal, nums)


def main():
    nums = [1,5,11,5]

    solution = Solution()

    result = solution.canPartition(nums)
    
    print(result)


if __name__ == "__main__":
    main()