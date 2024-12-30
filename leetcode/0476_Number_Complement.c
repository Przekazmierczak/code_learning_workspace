/*
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

Constraints:

1 <= num < 231
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int findComplement(int num) {
    int arr[32] = {0};
    int last1;
    int bit;
    int res = 0;
    
    for (int i = 0; i < 32; i++) {
        bit = num & 1;
        arr[i] = bit;
        if (bit) {
            last1 = i;
        }
        num = num >> 1;
    }
    
    for (int i = last1; i >= 0; i--) {
        res = res << 1;
        if (!arr[i]) {
            res ^= 1;
        }
    }
    
    return res;
}

int main() {
    int num = 5;

    int res = findComplement(num);

    printf("%d", res);

    return 0;
}