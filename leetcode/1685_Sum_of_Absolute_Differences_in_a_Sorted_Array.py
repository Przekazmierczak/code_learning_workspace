"""
You are given an integer array nums sorted in non-decreasing order.
Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

Example 1:
Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

Example 2:
Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]

Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
"""

class Solution:
    # def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    def getSumAbsoluteDifferences(self, nums):
        left, right = [], []
        curr_left, curr_right = 0, 0
        res = []
        
        for i in range(len(nums)):
            curr_left += nums[i]
            left.append(curr_left)
            curr_right += nums[len(nums) - 1 - i]
            right.append(curr_right)
        
        for i in range(len(nums)):
            res_left = left[i - 1] - (i * nums[i]) if (i - 1) >= 0 else 0
            
            res_right = right[len(nums) - 2 - i] - ((len(nums) - 1 - i) * nums[i]) if (len(nums) - 2 - i) >= 0 else 0
            res.append(res_right - res_left)
        
        return res
            

def main():
    nums = [2,3,5]

    solution = Solution()

    result = solution.getSumAbsoluteDifferences(nums)
    
    print(result)


if __name__ == "__main__":
    main()