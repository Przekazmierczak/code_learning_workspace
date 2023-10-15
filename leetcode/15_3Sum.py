"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        # Create a sorted copy of the 'nums' list.
        sorted_nums = nums.copy()
        sorted_nums.sort()

        # Create a list for the result
        result = []

        # Get the length of the 'sorted_nums' list.
        len_nums = len(sorted_nums)

        # Initialize the third index to start of the 'sorted_nums' list.
        third_index = 0
        

        for third_index in range(len_nums - 1):
        
            # Initialize two pointers: 'start_index' at the beginning and 'end_index' at the end of the sorted list.
            start_index = third_index + 1
            end_index = len_nums - 1

            # If the current element at 'third_index' is greater than 0, there are no more solutions. 
            if sorted_nums[third_index] > 0:
                break

            while start_index < end_index:

                # Calculate the sum of numbers pointed to by 'third_index', 'start_index' and 'end_index'.
                current_sum = sorted_nums[third_index] + sorted_nums[start_index] + sorted_nums[end_index]
                
                # If the current sum is greater than 0, move 'end_index' one position back.
                if current_sum > 0:
                    end_index -= 1
                # If the current sum is smaller than 0, move 'start_index' one position forward.
                elif current_sum < 0:
                    start_index += 1
                # If the current sum equals 0, we've found a solution.
                # Check if the new solution is not already in the 'result' list.
                else:
                    if [sorted_nums[third_index], sorted_nums[start_index], sorted_nums[end_index]] not in result:
                        result.append([sorted_nums[third_index], sorted_nums[start_index], sorted_nums[end_index]])
                    start_index += 1
        
        # Return the result
        return result

def main():
    nums = [-1,0,1,2,-1,-4]

    solution = Solution()

    result = solution.threeSum(nums)
    
    print(result)


if __name__ == "__main__":
    main()