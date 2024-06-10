"""
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""

class Solution:
    # def findNumberOfLIS(self, nums: List[int]) -> int:
    def findNumberOfLIS(self, nums):
        dp = [None] * len(nums)
        dp[0] = (1, 1)
        
        for i in range(1, len(nums)):
            count1 = 0
            count2 = 0
            curr_max = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if curr_max < dp[j][0]:
                        curr_max = dp[j][0]
                        count2 = 0
                    count1 = curr_max
                    if curr_max == dp[j][0]:
                        count2 += dp[j][1]
            count1 += 1
            count2 = max(count2, 1)
            dp[i] = (count1, count2)
        
        max_ = max(dp)
        res = 0
        for element in dp:
            if element[0] == max_[0]:
                res += element[1]
        return res
            

def main():
    nums = [1,3,5,4,7]

    solution = Solution()

    result = solution.findNumberOfLIS(nums)
    
    print(result)


if __name__ == "__main__":
    main()