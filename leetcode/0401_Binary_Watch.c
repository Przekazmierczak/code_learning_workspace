/*
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
For example, the below binary watch reads "4:51".

Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.
The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []

Constraints:

0 <= turnedOn <= 10
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

void helper(char** res, int* num, int* returnSize) {
    int hour = 0;
    int minutes = 0;
    for (int i = 0; i < 4; i++) {
        if (num[i]) {
            hour += pow(2, i);
        }
    }
    
    for (int i = 0; i < 6; i++) {
        if (num[i + 4]) {
            minutes += pow(2, i);
        }
    }
    
    if (hour < 12 && minutes < 60) {
        res[*returnSize] = malloc(10 * sizeof(char));
        sprintf(res[*returnSize], "%d:%02d", hour, minutes);
        (*returnSize)++;
    }
}

void backTrack(int* num, int position, int count, int turnedOn, char** res, int* returnSize) {
    if (count == turnedOn) {
        helper(res, num, returnSize);
        return;
    }
    
    position++;
    if (position < 10) {
        backTrack(num, position, count, turnedOn, res, returnSize);
        num[position] = 1;
        backTrack(num, position, count + 1, turnedOn, res, returnSize);
        num[position] = 0;
    }
}

char** readBinaryWatch(int turnedOn, int* returnSize) {
    char** res = malloc(200 * sizeof(char*));
    *returnSize = 0;
    int num[10] = {0};
    backTrack(num, -1, 0, turnedOn, res, returnSize);
    return res;
}

int main() {
    int turnedOn = 1;
    int x = 0;
    int* returnSize = &x;

    char** res = readBinaryWatch(turnedOn, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        printf("%s, ", res[i]);
    }

    return 0;
}