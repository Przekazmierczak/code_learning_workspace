"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        if k > len(nums):
            k = len(nums)
        
        visited = set()
        for i in range(k):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        
        for i in range(k, len(nums)):
            if nums[i] in visited:
                return True
            visited.remove(nums[i - k])
            visited.add(nums[i])
        
        return False

def main():
    nums = [1,2,3,1]
    k = 3

    solution = Solution()

    result = solution.containsNearbyDuplicate(nums, k)
    
    print(result)


if __name__ == "__main__":
    main()