"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45
"""

class Solution:
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
        memory = {}
        memory[1] = 1
        memory[2] = 2
        
        def step(n):
            if n in memory:
                return memory[n]
            else:
                memory[n] = step(n - 1) + step(n - 2)
                return memory[n]       
                
        return step(n)


def main():
    n = 3

    solution = Solution()

    result = solution.climbStairs(n)
    
    print(result)


if __name__ == "__main__":
    main()