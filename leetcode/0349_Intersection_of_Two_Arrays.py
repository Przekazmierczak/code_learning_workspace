"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        
        for num in set1:
            if num in set2:
                res.append(num)
        
        return res
            

def main():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    solution = Solution()

    result = solution.intersection(nums1, nums2)
    
    print(result)


if __name__ == "__main__":
    main()