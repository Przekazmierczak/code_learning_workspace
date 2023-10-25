"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    def addBinary(self, a, b):
        if len(a) >= len(b):
            longer = a[::-1]
            shorter = b[::-1]
            max_long_pointer = len(a) - 1
            max_short_pointer = len(b) - 1
            
        else:
            longer = b[::-1]
            shorter = a[::-1]
            max_long_pointer = len(b) - 1
            max_short_pointer = len(a) - 1
        
        pointer = 0
        result = ""
        
        reminder = False
        
        while pointer <= max_short_pointer:
            if longer[pointer] == "0" and shorter[pointer] == "0":
                if reminder == True:
                    reminder = False
                    result = "1" + result
                else:
                    result = "0" + result
                    
            elif longer[pointer] == "1" and shorter[pointer] == "1":
                if reminder == True:
                    result = "1" + result
                else:
                    reminder = True
                    result = "0" + result
                
            else:
                if reminder == True:
                    result = "0" + result
                else:
                    result = "1" + result
                    
            pointer += 1

        while reminder == True and pointer <= max_long_pointer:
            if longer[pointer] == "1":
                result = "0" + result
            else:
                result = "1" + result
                reminder = False
                
            pointer += 1
        
        if pointer <= max_long_pointer:
            result = longer[pointer:][::-1] + result
        
        if reminder == True:
            result = "1" + result
            
        return result



def main():
    a = "1010"
    b = "1011"

    solution = Solution()

    result = solution.addBinary(a, b)
    
    print(result)


if __name__ == "__main__":
    main()