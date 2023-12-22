"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
1 <= nums[i] <= 100
"""

class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums):
        dp = [1 for _ in range(len(nums))]
        longest = 0

        for i in range(len(dp) - 1, -1, -1):
            new_list = []
            for j in range(i + 1, len(dp)):
                if nums[i] < nums[j]:
                    new_list.append(dp[j])
            if new_list:
                dp[i] += max(new_list)
            longest = max(longest, dp[i])

        return longest

def main():
    nums = [10,9,2,5,3,7,101,18]

    solution = Solution()

    result = solution.lengthOfLIS(nums)
    
    print(result)


if __name__ == "__main__":
    main()