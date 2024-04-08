"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

class Solution:
    # def removeKdigits(self, num: str, k: int) -> str:
    def removeKdigits(self, num, k):
        stack = []
        
        for i in range(len(num)):
            while stack and k and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(num[i])
        
        while k:
            stack.pop()
            k -= 1
        
        if not stack:
            return "0"
        
        i = 0
        while stack[i] == "0" and i < len(stack) - 1:
            i += 1
        
        return "".join(stack[i:])
            

def main():
    num = "1432219"
    k = 3

    solution = Solution()

    result = solution.removeKdigits(num, k)
    
    print(result)


if __name__ == "__main__":
    main()