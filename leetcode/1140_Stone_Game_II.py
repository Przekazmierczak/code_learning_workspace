"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
"""

class Solution:
    # def stoneGameII(self, piles: List[int]) -> int:
    def stoneGameII(self, piles):
        memo = {}
        def dfs(i, m, alice):
            if i == len(piles):
                return 0
            
            if (i, m, alice) in memo:
                return memo[(i, m, alice)]
            
            if alice:
                res = 0
                total = 0
                for j in range(2 * m):
                    if i + j + 1 > len(piles):
                        break
                    total += piles[i + j]
                    res = max(dfs(i + j + 1, max(m, j + 1), False) + total, res)
            else:
                res = float("inf")
                for j in range(2 * m):
                    if i + j + 1 > len(piles):
                        break
                    res = min(dfs(i + j + 1, max(m, j + 1), True), res)
            memo[(i, m, alice)] = res
            return res
        
        return dfs(0, 1, True)
            

def main():
    piles = [1,2,3,4,5,100]

    solution = Solution()

    result = solution.stoneGameII(piles)
    
    print(result)


if __name__ == "__main__":
    main()