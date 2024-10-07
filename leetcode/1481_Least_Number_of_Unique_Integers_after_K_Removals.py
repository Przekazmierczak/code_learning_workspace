"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2

Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
import heapq

class Solution:
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    def findLeastNumOfUniqueInts(self, arr, k):
        dic = {}
        
        for num in arr:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
        
        heap = []
        heapq.heapify(heap)
        
        for key in dic:
            heapq.heappush(heap, dic[key])
            
        while k > 0 and heap:
            k = k - heapq.heappop(heap)
        
        return len(heap) if k == 0 else len(heap) + 1
            

def main():
    arr = [4,3,1,1,3,3,2]
    k = 3

    solution = Solution()

    result = solution.findLeastNumOfUniqueInts(arr, k)
    
    print(result)


if __name__ == "__main__":
    main()