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
        result = []
        used = []
        nums.sort()
        
        def subset(pointer):
            if not nums:
                return
            
            result.append(used[:])
            prev = None
            
            for index in range(pointer, len(nums)):
                if nums[index] != prev:
                    prev = nums[index]
                    used.append(nums[index])
                    subset(index + 1)
                    used.pop()
            
        subset(0)
        return result

def main():
    nums = [1,2,2]

    solution = Solution()

    result = solution.subsetsWithDup(nums)
    
    print(result)


if __name__ == "__main__":
    main()