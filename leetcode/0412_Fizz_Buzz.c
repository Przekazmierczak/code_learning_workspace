/*
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:

1 <= n <= 104
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    *returnSize = n;
    char** res = malloc(n * sizeof(char*));

    for (int i = 1; i <= n; i++) {
        char* str = malloc(10 * sizeof(char));
        if (!(i % 3) && !(i % 5)) {
            str = "FizzBuzz";
        } else if (!(i % 3)) {
            str = "Fizz";
        } else if (!(i % 5)) {
            str = "Buzz";
        } else {
            sprintf(str, "%d", i);
        }
        res[i - 1] = str;
    }
    
    return res;
}

int main() {
    int n = 5;
    int x = 5;
    int* returnSize = &x;

    char** res = fizzBuzz(n, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        printf("%s, ", res[i]);
    }

    return 0;
}