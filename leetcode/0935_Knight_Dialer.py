"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.
"""

class Solution:
    # def knightDialer(self, n: int) -> int:
    def knightDialer(self, n):
        neighbors = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        memo = {}
        def dfs(num, jumps):
            if jumps == 1:
                return 1
            if (num, jumps) in memo:
                return memo[(num, jumps)]
            result = 0
            for neighbor in neighbors[num]:
                result += dfs(neighbor, jumps - 1)
            memo[(num, jumps)] = result
            return result
        
        res = 0
        for i in range(10):
            res += dfs(i, n)
        return res % (10 ** 9 + 7)
            

def main():
    n = 222222

    solution = Solution()

    result = solution.knightDialer(n)
    
    print(result)


if __name__ == "__main__":
    main()