"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        pointer1 = 0
        pointer2 = 0
        
        max_pointer1 = len(nums1)
        max_pointer2 = len(nums2)

        nums3 = []

        while True:
            if pointer1 == max_pointer1:
                nums3.extend(nums2[pointer2:])
                break

            elif pointer2 == max_pointer2:
                nums3.extend(nums1[pointer1:])
                break

            elif nums1[pointer1] < nums2[pointer2]:
                nums3.append(nums1[pointer1])
                pointer1 += 1
            
            elif nums1[pointer1] > nums2[pointer2]:
                nums3.append(nums2[pointer2])
                pointer2 += 1
            
            else:
                nums3.append(nums1[pointer1])
                nums3.append(nums2[pointer2])
                pointer1 += 1
                pointer2 += 1
        
        len_nums3 = len(nums3)
        even_odd_check = len_nums3 % 2
        
        index = len_nums3 // 2

        if even_odd_check != 0:
            return nums3[index]
        else:
            return (nums3[index - 1] + nums3[index]) / 2
            

def main():
    nums1 = [1,3]
    nums2 = [2]

    solution = Solution()

    result = solution.findMedianSortedArrays(nums1, nums2)
    
    print(result)


if __name__ == "__main__":
    main()