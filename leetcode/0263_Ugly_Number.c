/*
An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:

-231 <= n <= 231 - 1
*/

#include <stdint.h>
#include <stdio.h>

int isUgly(int n) {
    if (n == 0) {
        return 0;
    }
    
    int primes[] = {5, 3, 2};
    
    for (int i = 0; i < 3; i++) {
        while (n % primes[i] == 0) {
            n /= primes[i];
        }
    }
    
    if (n != 1) {
        return 0;
    }
    
    return 1;
}

int main() {
    int n = 6;

    int res = isUgly(n);

    printf("%i", res);

    return 0;
}