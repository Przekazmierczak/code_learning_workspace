/*
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
Return the reformatted license key.

Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

Constraints:

1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

char* licenseKeyFormatting(char* s, int k) {
    int len = -1;
    int letters = 0;
    int dashes = 0;
    while (s[++len] != '\0') {
        if (s[len] != '-') {
            letters++;
        }
    }
    dashes = letters / k;
    if (!(letters % k)) {
        dashes--;
    }

    if (letters == 0) {
        return "";
    }

    int size = letters + dashes + 1;

    char* res = (char*)malloc(size * sizeof(char));
    res[size - 1] = '\0';

    int curr = size - 2;
    int currInK = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (s[i] != '-') {
            if (s[i] >= 97 && s[i] <= 122) {
                res[curr--] = s[i] - 32;
            } else {
                res[curr--] = s[i];
            }
            letters--;
            currInK++;
            if (currInK == k && letters != 0) {
                res[curr--] = '-';
                currInK = 0;
            }
        }

    }

    return res;
}

int main() {
    char* s = "5F3Z-2e-9-w";
    int k = 4;

    char* res = licenseKeyFormatting(s, k);

    int i = 0;
    while (res[i] != '\0'){
        printf("%c", res[i++]);
    }

    return 0;
}