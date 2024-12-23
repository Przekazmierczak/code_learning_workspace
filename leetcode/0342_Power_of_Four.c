/*
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true

Constraints:

-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
*/

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

int getBit(int num) {
    return num & 1;
}

bool isPowerOfFour(int n) {
    if (n <= 0) {
        return 0;
    }
    
    int bit;
    int curr = n;
    bool flag = false;
    
    for (int i = 0; i < 32; i++) {
        bit = getBit(curr);
        if (bit == 1) {
            if (i % 2 == 1 || flag == true) {
                return 0;
            }
            flag = true;
        }
        curr = curr >> 1;
    }
    return 1;
}

int main() {
    int n = 16;

    int res = isPowerOfFour(n);

    printf("%i", res);

    return 0;
}