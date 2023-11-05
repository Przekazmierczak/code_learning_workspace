"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 
Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    def firstMissingPositive(self, nums):
        length = len(nums)

        for i in range(length):
            if nums[i] < 0: nums[i] = 0

        for num in nums:
            abs_num = abs(num)
            if 0 < abs_num <= length:
                if nums[abs_num - 1] >= 0:
                    if nums[abs_num - 1] == 0:
                        nums[abs_num - 1] = -(length + 1)
                    else:
                        nums[abs_num - 1] *= -1

        for i in range(length):
            if nums[i] >= 0:
                return i + 1
        
        return length + 1

def main():
    nums = []

    solution = Solution()

    result = solution.firstMissingPositive(nums)
    
    print(result)


if __name__ == "__main__":
    main()