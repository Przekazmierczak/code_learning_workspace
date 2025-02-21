/*
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"

Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
*/

#include <string>

class Solution {
public:
    std::string toLowerCase(std::string s) {
        for (auto& i: s) {
            if (i >= 'A' && i <= 'Z') {
                i = i - 'A' + 'a';
            }
        }
        return s;
    }
};