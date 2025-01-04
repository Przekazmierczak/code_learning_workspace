/*
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false

Constraints:

1 <= num <= 10^8
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

bool checkPerfectNumber(int num) {
    if (num == 1) {
        return false;
    }
    
    int root = sqrt(num);
    int sum = 1;
    for (int i = 2; i <= root; i++) {
        if (!(num % i)) {
            sum += i;
            sum += num / i;
        }
    }
    if (sum == num) {
        return true;
    }
    return false;
}

int main() {
    int num = 28;

    int res = checkPerfectNumber(num);

    printf("%d", res);

    return 0;
}