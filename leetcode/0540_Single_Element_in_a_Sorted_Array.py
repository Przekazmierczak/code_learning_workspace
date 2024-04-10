"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""

class Solution:
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid != l and nums[mid] == nums[mid - 1]:
                if (l + mid - 1) % 2:
                    r = mid - 2
                else:
                    l = mid + 1
            elif mid != r and nums[mid] == nums[mid + 1]:         
                if (l + mid) % 2:
                    r = mid - 1
                else:
                    l = mid + 2
            else:
                return nums[mid]
            

def main():
    nums = [1,1,2,3,3,4,4,8,8]

    solution = Solution()

    result = solution.singleNonDuplicate(nums)
    
    print(result)


if __name__ == "__main__":
    main()