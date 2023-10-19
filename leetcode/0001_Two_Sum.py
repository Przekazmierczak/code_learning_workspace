"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        # Create a sorted copy of the 'nums' list.
        sorted_nums = nums.copy()
        sorted_nums.sort()
        
        # Initialize two pointers: 'start' at the beginning and 'end' at the end of the sorted list.
        start = 0
        end = len(sorted_nums) - 1

        while True:
            # Calculate the sum of numbers pointed to by 'start' and 'end'.
            check = sorted_nums[start] + sorted_nums[end]
            
            # If the current sum is greater than the target, move 'end' one position back.
            if check > target:
                end -= 1
            # If the current sum is smaller than the target, move 'start' one position forward.
            elif check < target:
                start += 1
            # If the current sum equals the target, we've found the solution.
            else:
                result = [start, end]
                break
        
        # If 'nums' was already sorted return the result.
        if nums == sorted_nums:
            return result
        
        # If not we need to retrieve the original indices for the two numbers in the 'nums' list.
        else:
            # Create new indexes.
            new_start = None
            new_end = None

            for index, number in enumerate(nums):
                # Locate the first number and add its index to the result.
                if number == sorted_nums[start] and new_start == None:
                    new_start = index
                # Locate the second number and add its index to the result.
                if number == sorted_nums[end] and new_start != index:
                    new_end = index
                # If we have already found both numbers, break the loop.
                if new_start != None and new_end != None:
                    break

            # Add new indexes to the result.
            result = [new_start, new_end]

            # Return the updated result.
            return result
            

def main():
    nums = [3, 2, 3]
    target = 6

    solution = Solution()

    result = solution.twoSum(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()