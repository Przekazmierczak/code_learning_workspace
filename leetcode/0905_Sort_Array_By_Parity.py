"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

class Solution:
    # def sortArrayByParity(self, nums: List[int]) -> List[int]:
    def sortArrayByParity(self, nums):
        l, r = 0, len(nums) - 1
        
        while l < r:
            if not nums[l] % 2:
                l += 1
            elif nums[r] % 2:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return nums
            

def main():
    nums = [3,1,2,4]

    solution = Solution()

    result = solution.sortArrayByParity(nums)
    
    print(result)


if __name__ == "__main__":
    main()