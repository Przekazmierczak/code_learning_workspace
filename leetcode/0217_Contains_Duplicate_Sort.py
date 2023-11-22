"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    def containsDuplicate(self, nums):
        nums.sort()
        previous = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == previous:
                return True
            
            previous= nums[i]
            
        return False

def main():
    nums = [1,2,3,1]

    solution = Solution()

    result = solution.containsDuplicate(nums)
    
    print(result)


if __name__ == "__main__":
    main()