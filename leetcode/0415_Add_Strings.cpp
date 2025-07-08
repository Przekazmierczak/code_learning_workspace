/*
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
'
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
*/

#include <iostream>
#include <string>

class Solution {
public:
    std::string addStrings(std::string num1, std::string num2) {
        int lenNum1 = num1.size();
        int lenNum2 = num2.size();
        
        int longer = std::max(num1.size(), num2.size());
        
        int currNum1;
        int currNum2;
        int carry = 0;
        int curr;
        
        std::string res;
        for (int i = 1; i <= longer; i++) {
            currNum1 = 0;
            if (lenNum1 - i >= 0) {
                currNum1 = num1[lenNum1 - i] - '0';
            }
        
            currNum2 = 0;
            if (lenNum2 - i >= 0) {
                currNum2 = num2[lenNum2 - i] - '0';
            }
        
            curr = currNum1 + currNum2 + carry;
            carry = curr / 10;
        
            res += curr % 10 + '0';
        }
        
        if (carry) {
            res += '1';
        }
        
        reverse(res.begin(), res.end());
        return res;
    }
};