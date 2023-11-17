"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        nums_len = len(nums)
        
        def result(nums, current_array, pointer):
            if current_array not in res:
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
    nums = [1,2,2]

    solution = Solution()

    result = solution.subsetsWithDup(nums)
    
    print(result)


if __name__ == "__main__":
    main()