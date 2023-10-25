"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while True:
            half = (left + right) // 2
            
            if target < nums[half]:
                right = half
            elif target > nums[half]:
                left = half           
            else:
                return half
            
            if right - left <= 1:
                if target <= nums[left]:
                    return left
                elif target <= nums[right]:
                    return right
                else:
                    return right + 1


def main():
    nums = [1,3,5,6]
    target = 7

    solution = Solution()

    result = solution.searchInsert(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()