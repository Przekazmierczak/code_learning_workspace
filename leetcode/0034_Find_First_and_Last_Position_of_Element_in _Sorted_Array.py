"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange(self, nums, target):
        def search(nums, target, beg, end):
            mid = (beg + end) // 2
            if beg > end:
                return [-1, -1]
            
            elif target < nums[mid]:
                return search(nums, target, beg, mid -1)
            
            elif target > nums[mid]:
                return search(nums, target, mid + 1, end)
            
            else:
                first = mid
                last = mid
                

                while first - 1 >= 0 and nums[first - 1] == target:
                    first -= 1
                    
                while last + 1 < len(nums) and nums[last + 1] == target:
                    last += 1

                return [first, last]
                    
        beg = 0
        end = len(nums) - 1
        
        return search(nums, target, beg, end)


def main():
    nums = [5,7,7,8,8,10]
    target = 8

    solution = Solution()

    result = solution.searchRange(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()