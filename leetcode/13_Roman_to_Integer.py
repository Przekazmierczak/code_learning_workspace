"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution:
    # def romanToInt(self, s: str) -> int:
    def romanToInt(self, s):
        roman_symbols_single = {"M": 1000, "D": 500,  "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        roman_symbols_double = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}

        pointer = 0
        number = 0

        while pointer < len(s):
            if (pointer + 1 < len(s)) and ((s[pointer] + s[pointer + 1]) in roman_symbols_double):
                number += roman_symbols_double[(s[pointer] + s[pointer + 1])]
                pointer += 2
            else:
                number += roman_symbols_single[s[pointer]]
                pointer += 1
        
        return number

def main():
    s = "MCMXCIV"

    solution = Solution()

    result = solution.romanToInt(s)
    
    print(result)


if __name__ == "__main__":
    main()