"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""

class Solution:
    # def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    def canPartitionKSubsets(self, nums, k):
        def backtrack(i, k, curr, target):
            if k == 0:
                return True
            
            if curr == target:
                return backtrack(0, k - 1, 0, target)
            
            for j in range(i, len(nums)):
                if j in visit or curr + nums[j] > target:
                    continue
                if j > 0 and (j - 1) not in visit and nums[j-1] == nums[j]:
                    continue
                visit.add(j)
                if backtrack(j + 1, k, curr + nums[j], target):
                    return True
                visit.remove(j)
            return False
        
        target = sum(nums) / k
        nums.sort(reverse=True)
        visit = set()
        
        return backtrack(0, k, 0, target)
            

def main():
    nums = [4,3,2,3,5,2,1]
    k = 4

    solution = Solution()

    result = solution.canPartitionKSubsets(nums, k)
    
    print(result)


if __name__ == "__main__":
    main()