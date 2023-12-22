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
        print(goal)

        sums = set()
        sums.add(0)

        for num in nums:
            to_add = []
            for curr_sum in sums:
                if curr_sum + num == goal:
                    return True
                if curr_sum + num < goal:
                    to_add.append(curr_sum + num)
            for element in to_add:
                sums.add(element)
        return False


def main():
    nums = [1,2,3,4,5,6,7]

    solution = Solution()

    result = solution.canPartition(nums)
    
    print(result)


if __name__ == "__main__":
    main()