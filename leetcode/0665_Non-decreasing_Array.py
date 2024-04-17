"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You cannot get a non-decreasing array by modifying at most one element.
 
Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""

class Solution:
    # def checkPossibility(self, nums: List[int]) -> bool:
    def checkPossibility(self, nums):
        def swap_curr(i, temp, nums):
            nums[i] = nums[i - 1]
            if (i + 1 >= len(nums) or nums[i] <= nums[i + 1]):
                nums[i] = temp
                return True
            nums[i] = temp
            return False
            
        def swap_prev(i, nums):
            nums[i - 1] = nums[i]
            if i - 2 < 0 or nums[i - 1] >= nums[i - 2]:
                return True
            return False
        
        swapped = False
        i = 1
        while i < len(nums):
            if nums[i - 1] > nums[i]:
                if not swapped:
                    if swap_curr(i, nums[i], nums) or swap_prev(i, nums):
                        swapped = True
                    else:
                        return False
                else:
                    return False
            i += 1
        return True
            

def main():
    nums = [4,2,3]

    solution = Solution()

    result = solution.checkPossibility(nums)
    
    print(result)


if __name__ == "__main__":
    main()