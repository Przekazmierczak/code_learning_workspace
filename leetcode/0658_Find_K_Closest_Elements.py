"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""

class Solution:
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    def findClosestElements(self, arr, k, x):
        def bs(arr, x):
            l, r = 0, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                
                if x > arr[mid]:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        i = bs(arr,x)
        if i == 0 or abs(arr[i] - x) < abs(arr[i - 1] - x):
            first = i
        else: 
            first = i -1
        
        l, r = first, first
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1:
                l -= 1
            elif abs(arr[l - 1] - x) > abs(arr[r + 1] - x):
                r += 1
            else:
                l -= 1
        
        return arr[l: r + 1]
            

def main():
    arr = [1,2,3,4,5]
    k = 4
    x = 3

    solution = Solution()

    result = solution.findClosestElements(arr, k, x)
    
    print(result)


if __name__ == "__main__":
    main()