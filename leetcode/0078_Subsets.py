"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    def subsets(self, nums):
        res = []
        nums_len = len(nums)
        
        def result(nums, current_array, pointer):
            res.append(current_array.copy())
            
            if pointer == nums_len:
                return
            
            for i in range(pointer, nums_len):
                new_array = current_array.copy()
                new_array.append(nums[i])
                result(nums, new_array, i + 1)
        
        result(nums, [], 0)
        
        return res
    

def main():
    nums = [1,2,3]

    solution = Solution()

    result = solution.subsets(nums)
    
    print(result)


if __name__ == "__main__":
    main()