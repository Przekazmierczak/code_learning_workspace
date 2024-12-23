/*
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
*/

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    *returnSize = 0;
    if (numsSize == 0) {
        return NULL; 
    }
    
    char **res = malloc(50*sizeof(char*));
    char *buffer = malloc(50* sizeof(char));
    
    int first = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if ((i == numsSize - 1) || (nums[i] + 1 != nums[i + 1])) {
            if (first !=  nums[i]) {
                sprintf(buffer, "%d->%d", first, nums[i]);
            } else {
                sprintf(buffer, "%d", nums[i]);
            }
            res[(*returnSize)++] = strdup(buffer);
            if (i < numsSize -1) {
                first = nums[i+1];
            }
        }
    }
    return res;
}

int main() {
    int nums[] = {0,2,3,4,6,8,9};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize = 0;

    char **res = summaryRanges(nums, numsSize, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", res[i]);
        free(res[i]);
    }
    free(res);

    return 0;
}