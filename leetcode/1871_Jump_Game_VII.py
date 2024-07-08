"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""

class Solution:
    # def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    def canReach(self, s, minJump, maxJump):
        jumps = maxJump - minJump + 1
        dp = [0] * len(s)
        dp[minJump] = 1
        step = 0
        
        for i in range(len(s)):
            step -= 1
            if dp[i] == 1:
                step = jumps
                
            if step > 0:
                if s[i] == "0" and i + minJump < len(s):
                    dp[i + minJump] = 1
                dp[i] = 1
        
        return dp[-1] if s[-1] == "0" else 0
            

def main():
    s = "011010"
    minJump = 2
    maxJump = 3

    solution = Solution()

    result = solution.canReach(s, minJump, maxJump)
    
    print(result)


if __name__ == "__main__":
    main()