/*
Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"

Constraints:

-231 <= num <= 231 - 1
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

char toString(int num, char* map) {
    if (num < 10) {
        return num + '0';
    }
    return map[num - 10];
}

char* toHex(int num) {
    if (num == 0) {
        return "0";
    }
    
    char* res = malloc(9 * sizeof(char));
    int resPosition = 0;
    char map[6] = {'a', 'b', 'c', 'd', 'e', 'f'};
    int curr;
    char buffer[8];
    int bufferPosition = 7;
    
    for (int i = 0; i < 32; i = i + 4) {
        curr = 0;
        for (int j = 0; j < 4; j++) {
            if (num & 1) {
                curr += pow(2, j);
            }
            num = num >> 1;
        }
        buffer[bufferPosition--] = toString(curr, map);
    }
    
    bool lead0 = true;
    for (int i = 0; i < 8; i++) {
        if (buffer[i] != '0' || lead0 == false) {
            res[resPosition++] = buffer[i];
            lead0 = false;
        }
    }
    res[resPosition] = '\0';
    
    return res;
}

int main() {
    int num = 26;

    char *res = toHex(num);

    printf("%s", res);

    return 0;
}