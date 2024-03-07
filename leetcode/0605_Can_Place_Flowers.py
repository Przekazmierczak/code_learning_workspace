"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    def canPlaceFlowers(self, flowerbed, n):
        prev, curr, nxt = 0, 1, 2
        bed = [0] + flowerbed + [0]
        
        for _ in range(len(flowerbed)):
            if not bed[prev] and not bed[curr] and not bed[nxt]:
                n -= 1
                bed[curr] = 1
            if n <= 0:
                return True
            prev += 1
            curr += 1
            nxt += 1
        return False
            

def main():
    flowerbed = [1,0,0,0,1]
    n = 2

    solution = Solution()

    result = solution.canPlaceFlowers(flowerbed, n)
    
    print(result)


if __name__ == "__main__":
    main()