/*
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:

3 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int maximumProduct(int* nums, int numsSize) {
    int max[3] = {-1001, -1001, -1001};
    int min[2] = {1001, 1001};
    int curr;
    int temp;

    for (int i = 0; i < numsSize; i++) {
        curr = nums[i];
        for (int j = 0; j < 3; j++) {
            if (curr > max[j]) {
                temp = max[j];
                max[j] = curr;
                curr = temp;
            }
        }
        curr = nums[i];
        for (int j = 0; j < 2; j++) {
            if (curr < min[j]) {
                temp = min[j];
                min[j] = curr;
                curr = temp;
            }
        }
    }
    int res1 = max[0] * max[1] * max[2];
    int res2 = min[0] * min[1] * max[0];
    
    return (res1 > res2) ? res1 : res2;
}

int main() {
    int nums[] = {1,2,3,4};

    int res = maximumProduct(nums, 4);

    printf("%d", res);

    return 0;
}