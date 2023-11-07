"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        
        def recursive(nums, track):
            if nums == []:
                ans.append(track[:])
                return
            
            for index in range(len(nums)):
                if index + 1 < len(nums) and nums[index] == nums[index + 1]:
                    continue
                    
                track.append(nums[index])
                new_nums = nums[:index] + nums[index+1:]
                recursive(new_nums, track)
                track.pop()
                
        recursive(nums, [])
        return ans



def main():
    nums = [1,1,2]

    solution = Solution()

    result = solution.permuteUnique(nums)
    
    print(result)


if __name__ == "__main__":
    main()