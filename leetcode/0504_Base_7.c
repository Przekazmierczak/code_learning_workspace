/*
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:

-107 <= num <= 107
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void helper(int* position, char* res, int* curr, int* resSize) {
    int power = pow(7, *position);
    if (*curr / power > 0) {
        (*position)++;
        helper(position, res, curr, resSize);
    } else {
        if (*position == 0) {
            res[(*resSize)++] = '0';
        }
        return;
    }
    res[(*resSize)++] = (*curr / power) + '0';
    *curr %= power;
}

char* convertToBase7(int num) {
    int* curr = malloc(sizeof(int));
    *curr = num;
    
    int* position = malloc(sizeof(int));
    *position = 0;
    
    int* resSize = malloc(sizeof(int));
    *resSize = 0;
    
    char* res = malloc(20 * sizeof(char));
    
    if (*curr < 0) {
        res[(*resSize)++] = '-';
        *curr = -*curr;
    }
    
    helper(position, res, curr, resSize);
    res[(*resSize)++] = '\0';
    
    free(curr);
    free(position);
    free(resSize);
    
    return res; 
}

int main() {
    int num = 100;

    char* res = convertToBase7(num);

    printf("%s", res);

    return 0;
}