"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 
Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest(self, nums, target):
        sorted_nums = sorted(nums)

        closest = None

        for third_index, third in enumerate(sorted_nums):
            left = third_index + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = third + sorted_nums[right] + sorted_nums[left]
                
                if closest == None:
                    closest = current_sum

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        return closest

def main():
    nums = [0,0,0]

    target = 10000

    solution = Solution()

    result = solution.threeSumClosest(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()