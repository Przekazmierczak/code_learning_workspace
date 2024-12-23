/*
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:

0 <= num <= 231 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
*/

#include <stdint.h>
#include <stdio.h>

int currSum(int currNum) {
    char str[11];
    int res = 0;
    int i = 0;
    
    sprintf(str, "%d", currNum);
    
    while (str[i] != '\0') {
        res += str[i++] - '0';
    }
    
    return res;
}

int addDigits(int num) {
    int res;
    
    do {
        res = currSum(num);
        num = res;
    } while (res > 9);
    
    return res;
}

int main() {
    int num = 38;

    int res = addDigits(num);

    printf("%i", res);

    return 0;
}