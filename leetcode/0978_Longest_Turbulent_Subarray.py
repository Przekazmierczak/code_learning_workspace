"""
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:

Input: arr = [4,8,12,16]
Output: 2

Example 3:

Input: arr = [100]
Output: 1

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""

class Solution:
    # def maxTurbulenceSize(self, arr: List[int]) -> int:
    def maxTurbulenceSize(self, arr):
        def check(i, odd):
            if odd:
                if arr[i] < arr[i + 1]:
                    return True
            if not odd:
                if arr[i] > arr[i + 1]:
                    return True
            return False
        
        curr1, curr2 = 0, 0
        global_max1, global_max2 = 0, 0
        
        for i in range(len(arr) - 1):
            if i % 2:
                if check(i, True):
                    curr1 += 1
                    global_max1 = max(global_max1, curr1)
                else:
                    curr1 = 0
                if check(i, False):
                    curr2 += 1
                    global_max2 = max(global_max2, curr2)
                else:
                    curr2 = 0
                    
            else:
                if check(i, False):
                    curr1 += 1
                    global_max1 = max(global_max1, curr1)
                else:
                    curr1 = 0
                if check(i, True):
                    curr2 += 1
                    global_max2 = max(global_max2, curr2)
                else:
                    curr2 = 0
            
        return max(global_max1, global_max2) + 1
            

def main():
    arr = [9,4,2,10,7,8,8,1,9]

    solution = Solution()

    result = solution.maxTurbulenceSize(arr)
    
    print(result)


if __name__ == "__main__":
    main()