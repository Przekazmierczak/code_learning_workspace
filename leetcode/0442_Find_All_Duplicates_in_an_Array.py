"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
"""

class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
    def findDuplicates(self, nums):
        res = []
        
        for num in nums:
            curr = abs(num)
            if nums[curr - 1] > 0:
                nums[curr - 1] *= -1
            else:
                res.append(curr)
        
        return res
            

def main():
    nums = [4,3,2,7,8,2,3,1]

    solution = Solution()

    result = solution.findDuplicates(nums)
    
    print(result)


if __name__ == "__main__":
    main()