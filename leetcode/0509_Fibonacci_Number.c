/*
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

int fibHelper(int n, int* memo) {
    if (memo[n] != -1) {
        return memo[n];
    } 
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    
    int res = fibHelper(n - 1, memo) + fibHelper(n - 2, memo);
    memo[n] = res;
    
    return res;
}

int fib(int n){
    int memo[31];
    for (int i = 0; i < 31; i++) {
        memo[i] = -1;
    }
    
    return fibHelper(n, memo);
}

int main() {
    int n = 4;

    int res = fib(n);

    printf("%d", res);

    return 0;
}