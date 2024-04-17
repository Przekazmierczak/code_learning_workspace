"""
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""

class Solution:
    # def findPeakElement(self, nums: List[int]) -> int:
    def findPeakElement(self, nums):
        LEN = len(nums) - 1
        l, r = 0, LEN
        
        while l <= r:
            mid = (l + r) // 2
            
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == LEN or nums[mid] > nums[mid + 1]):
                return mid
                
            elif (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == LEN or nums[mid] < nums[mid + 1]):
                l = mid + 1
            else:
                r = mid - 1
            

def main():
    nums = [1,2,1,3,5,6,4]

    solution = Solution()

    result = solution.findPeakElement(nums)
    
    print(result)


if __name__ == "__main__":
    main()