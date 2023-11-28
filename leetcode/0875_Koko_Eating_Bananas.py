"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 
Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from math import ceil

class Solution:
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    def minEatingSpeed(self, piles, h):
        def check_if_koko_is_happy(k):
            happiness = 0
            for pile in piles:
                happiness += ceil(pile / k)
            return happiness <= h
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            check = check_if_koko_is_happy(mid)

            if check:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

def main():
    piles = [1, 1]
    h = 2

    solution = Solution()

    result = solution.minEatingSpeed(piles, h)
    
    print(result)


if __name__ == "__main__":
    main()