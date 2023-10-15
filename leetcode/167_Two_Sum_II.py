"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):
        # Initialize two pointers: 'start' at the beginning and 'end' at the end of the sorted list.
        start = 0
        end = len(numbers) - 1

        while True:
            # Calculate the sum of numbers pointed to by 'start' and 'end'.
            check = numbers[start] + numbers[end]
            
            # If the current sum is greater than the target, move 'end' one position back.
            if check > target:
                end -= 1
            # If the current sum is smaller than the target, move 'start' one position forward.
            elif check < target:
                start += 1
            # If the current sum equals the target, we've found the solution.
            else:
                result = [start + 1, end + 1]
                return result
            

def main():
    nums = [2,7,11,15]
    target = 9

    solution = Solution()

    result = solution.twoSum(nums, target)
    
    print(result)


if __name__ == "__main__":
    main()