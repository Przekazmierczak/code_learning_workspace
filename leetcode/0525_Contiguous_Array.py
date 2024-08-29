"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]

Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    def findMaxLength(self, nums):
        count = {0: -1}
        curr = 0
        res = 0
        
        for i in range(len(nums)):
            value = 1 if nums[i] else - 1
            curr += value
            
            if curr not in count:
                count[curr] = i
            elif curr in count:
                res = max(res, i - count[curr])
                
        return res
            

def main():
    nums = [0,1,0]

    solution = Solution()

    result = solution.findMaxLength(nums)
    
    print(result)


if __name__ == "__main__":
    main()