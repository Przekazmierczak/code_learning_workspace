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

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

char* addStrings(char* num1, char* num2) {
    int lenNum1 = 0;
    int lenNum2 = 0;
    while (num1[lenNum1] != '\0') {
        lenNum1++;
    }
    while (num2[lenNum2] != '\0') {
        lenNum2++;
    }

    int longer;
    if (lenNum1 > lenNum2) {
        longer = lenNum1;
    } else {
        longer = lenNum2;
    }

    int currNum1;
    int currNum2;
    int carry = 0;
    int curr;
    char* res = malloc((pow(10, 4) + 2) * sizeof(char));
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

        res[longer - i + 1] = curr % 10 + '0';
    }
    res[0] = '1';
    res[longer + 1] = '\0';
    
    if (!carry) {
        res++;
    }
    return res;
}

int main() {
    char* num1 = "456";
    char* num2 = "77";

    char* res = addStrings(num1, num2);

    printf("%s", res);

    return 0;
}