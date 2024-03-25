"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""

class Solution:
    # def minFlips(self, s: str) -> int:
    def minFlips(self, s):
        LEN = len(s)
        l, r = 0, LEN - 1
        first, second = "", ""
        res = float("inf")
        s = s + s
        
        for i in range(len(s)):
            first += "0" if i % 2 else "1"
            second += "1" if i % 2 else "0"

        count_first_string = bin(int(s[:LEN], 2) ^ int(first[:LEN], 2))
        count_second_string = bin(int(s[:LEN], 2) ^ int(second[:LEN], 2))
        
        count_first = count_first_string.count("1")
        count_second = count_second_string.count("1")
        
        while r < len(s) - 1:
            r += 1
            if s[r] != first[r]:
                count_first += 1
            if s[l] != first[l]:
                count_first -= 1
            if s[r] != second[r]:
                count_second += 1
            if s[l] != second[l]:
                count_second -= 1
            l += 1
            res = min(res, count_first, count_second)
            
        return res
            

def main():
    s = "111000"

    solution = Solution()

    result = solution.minFlips(s)
    
    print(result)


if __name__ == "__main__":
    main()