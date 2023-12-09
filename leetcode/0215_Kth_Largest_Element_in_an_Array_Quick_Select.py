"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import random

class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        left, mid, right = [], [], []

        for element in nums:
            if element > pivot:
                left.append(element)
            elif element < pivot:
                right.append(element)
            else:
                mid.append(element)

        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return mid[0]


def main():
    nums = [3,2,1,5,6,4]
    k = 2

    solution = Solution()

    result = solution.findKthLargest(nums, k)
    
    print(result)


if __name__ == "__main__":
    main()