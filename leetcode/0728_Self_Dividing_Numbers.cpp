/*
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

Example 1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
Input: left = 47, right = 85
Output: [48,55,66,77]

Constraints:

1 <= left <= right <= 104
*/

#include <vector>

class Solution {
public:
    bool ifDiviNum(int num) {
        int copy = num;
        int curr;
        while (copy) {
            curr = copy % 10;
            if (!curr || num % curr) {
                return false;
            }
            copy /= 10;
        }
        return true;
    }
    
    std::vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> res;
        for (int i = left; i < right + 1; i++) {
            if (ifDiviNum(i)) {
                res.push_back(i);
            }
        }
        return res;
    }
};