"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""

class Solution:
    def compare(self, l1, r1, l2, r2, nums):
        left, right = nums[l1:r1+1], nums[l2:r2+1]
        i, j, k = 0, 0, l1

        while i < len(left) and j < len(right):
            first = left[i] + right[j]
            second = right[j] + left[i]
            if first > second:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, l, r, nums):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(l, mid, nums)
            self.mergeSort(mid + 1, r, nums)
            self.compare(l, mid, mid + 1, r, nums)

    # def largestNumber(self, nums: List[int]) -> str:
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        self.mergeSort(0, len(nums) - 1, nums)

        return "0" if nums[0] == 0 else "".join(nums)



def main():
    nums = [3,30,34,5,9]

    solution = Solution()

    result = solution.largestNumber(nums)
    
    print(result)


if __name__ == "__main__":
    main()