/*
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:

n == nums.length
1 <= k <= n <= 10^5
-104 <= nums[i] <= 10^4
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

double findMaxAverage(int* nums, int numsSize, int k) {
    double curr = 0;
    double max = -pow(10, 4);

    for (int i = 0; i < numsSize; i++) {
        curr += (double)nums[i] / k;
        if (i >= k - 1) {
            max = (max >= curr) ? max : curr;
            curr -= (double)nums[i - k + 1] / k;
        }
    }

    return max;
}

int main() {
    int nums[] = {1,12,-5,-6,50,3};
    int numsSize = 6;
    int k = 4;

    double res = findMaxAverage(nums, numsSize, k);

    printf("%f", res);

    return 0;
}