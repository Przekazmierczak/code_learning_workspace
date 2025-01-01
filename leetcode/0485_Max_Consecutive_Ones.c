/*
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int res = 0;
    int curr = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            curr++;
            if (curr > res) {
                res = curr;
            }
        } else {
            curr = 0;
        }
    }
    return res;
}

int main() {
    int nums[] = {1,1,0,1,1,1};
    int numsSize = 6;

    int res = findMaxConsecutiveOnes(nums, numsSize);
    printf("%d", res);

    return 0;
}