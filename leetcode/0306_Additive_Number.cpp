/*
An additive number is a string whose digits can form an additive sequence.
A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
Given a string containing only digits, return true if it is an additive number or false otherwise.
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

Constraints:

1 <= num.length <= 35
num consists only of digits.

Follow up: How would you handle overflow for very large input integers?
*/

#include <iostream>
#include <string>

class Solution {
public:
    //leetcode 415
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
    
    bool check(std::string first, std::string second, int index, std::string& num) {
    std::string third = addStrings(first, second);
    int new_index = index + third.size();

        if (new_index > num.size()) return false;
        if (num.substr(index, third.size()) == third) {
            if (new_index == num.size()) return true;
            return check(second, third, new_index, num);
        }
        return false;
    }

    bool isAdditiveNumber(std::string num) {
        for (int i = 1; i < num.size() / 2 + 1; i++) {
            if (num[0] == '0' && i > 1) return false;
            for (int j = 1; std::max(i, j) < num.size() - i - j + 1; j++) {
                if (num[i] == '0' && j > 1) break;
                
                if (check(num.substr(0, i), num.substr(i, j), i + j, num)) {
                    return true;
                }
            }
        }
        return false;
    }
};