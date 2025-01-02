/*
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

Example 1:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Example 2:
Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    int maxScore = 0;
    for (int i = 0; i < scoreSize; i++) {
        if (score[i] > maxScore) {
            maxScore = score[i];
        }
    }

    *returnSize = scoreSize;
    char** res = malloc(*returnSize * sizeof(char*));
    int* scores = malloc((maxScore + 1) * sizeof(int));

    for (int i = 0; i < maxScore + 1; i++) {
        scores[i] = -1;
    }

    for (int i = 0; i < scoreSize; i++) {
        scores[score[i]] = i;
    }

    int place = 1;
    for (int i = maxScore ; i >= 0; i--) {
        if (scores[i] != -1) {
            res[scores[i]] = malloc(20 * sizeof(char));
            if (place == 1) {
                res[scores[i]] = "Gold Medal";
            } else if (place == 2) {
                res[scores[i]] = "Silver Medal";
            } else if (place == 3) {
                res[scores[i]] = "Bronze Medal";
            } else {
                sprintf(res[scores[i]], "%d", place);
            }
            place++;
        }
    }

    return res;
}

int main() {
    int score[] = {5,4,3,2,1};
    int scoreSize = 5;
    int* returnSize = malloc(sizeof(int));
    *returnSize = 5;


    char** res = findRelativeRanks(score, scoreSize, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        printf("%s\n", res[i]);
    }

    return 0;
}