"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    def sortArray(self, nums):
        def sort(left, right):
            if left == right:
                return [nums[right]]
            
            mid = (left + right) // 2
            lList = sort(left, mid)
            rList = sort(mid + 1, right)
            l, r = 0, 0
            newList = []
            
            while l < len(lList) and r < len(rList):
                if lList[l] < rList[r]:
                    newList.append(lList[l])
                    l += 1
                else:
                    newList.append(rList[r])
                    r += 1
                
            if l < len(lList):
                newList.extend(lList[l:])
            elif r < len(rList):
                newList.extend(rList[r:])
                
            return newList
        return sort(0, len(nums) - 1)
            

def main():
    arr = [5,1,1,2,0,0]

    solution = Solution()

    result = solution.sortArray(arr)
    
    print(result)


if __name__ == "__main__":
    main()