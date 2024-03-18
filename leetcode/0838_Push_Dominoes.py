"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.
"""

class Solution:
    # def pushDominoes(self, dominoes: str) -> str:
    def pushDominoes(self, dominoes):
        prev = ("L", -1)
        res = []
        for c in dominoes:
            res.append(c)
        res.append("R")
        i = 0
        
        while i < len(res):
            if res[i] == "L":
                if prev[0] == "L":
                    for j in range(prev[1] + 1, i):
                        res[j] = "L"
                else:
                    l,r = prev[1] + 1, i - 1
                    while r - l > 0:
                        res[l], res[r] = "R", "L"
                        l += 1
                        r -= 1
                prev = ("L", i)
                    
            elif res[i] == "R":
                if prev[0] == "R":
                    for j in range(prev[1] + 1, i):
                        res[j] = "R"
                prev = ("R", i)
            i += 1
            
        return "".join(res[:-1]) 
            

def main():
    dominoes = ".L.R...LR..L.."

    solution = Solution()

    result = solution.pushDominoes(dominoes)
    
    print(result)


if __name__ == "__main__":
    main()