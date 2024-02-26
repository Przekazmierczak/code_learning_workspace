"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""

class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    def sortedSquares(self, nums):
        l, r = 0, len(nums) - 1
        res = []
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= 0:
                r = mid - 1
            else:
                l = mid + 1
        
        pos, neg = l, l - 1
        
        while neg >= 0 and pos < len(nums):
            if abs(nums[pos]) <= abs(nums[neg]):
                res.append(nums[pos] ** 2)
                pos += 1
            else:
                res.append(nums[neg] ** 2)
                neg -= 1
                
        while neg >= 0:
            res.append(nums[neg] ** 2)
            neg -= 1
            
        while pos < len(nums):
            res.append(nums[pos] ** 2)
            pos += 1
        
        return res
            

def main():
    nums = [-4,-1,0,3,10]

    solution = Solution()

    result = solution.sortedSquares(nums)
    
    print(result)


if __name__ == "__main__":
    main()