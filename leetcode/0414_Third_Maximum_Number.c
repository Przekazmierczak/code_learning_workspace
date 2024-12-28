/*
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int thirdMax(int* nums, int numsSize) {
    int array[3] = {INT_MIN, INT_MIN, INT_MIN};
    int temp;
    int unique = 0;
    bool ifINT_MIN = false;

    for (int i = 0; i < numsSize; i++) {
        int curr = nums[i];
        if (nums[i] == INT_MIN && !ifINT_MIN) {
            unique++;
            ifINT_MIN = true;
            continue;
        }
        if (curr == array[0] || curr == array[1] || curr == array[2]) {
            continue;
        }
        if (curr > array[0]) {
            temp = array[0];
            array[0] = curr;
            curr = temp;
        }
        if (curr > array[1]) {
            temp = array[1];
            array[1] = curr;
            curr = temp;
            unique++;
        }
        if (curr > array[2]) {
            temp = array[2];
            array[2] = curr;
            curr = temp;
            unique++;
        }
    }
    if (unique < 2) {
        unique = 0;
    } else {
        unique = 2;
    }
    return array[unique];
}

int main() {
    int nums[4] = {2,2,3,1};
    int numsSize = 4;

    int res = thirdMax(nums, numsSize);

    printf("%d", res);

    return 0;
}