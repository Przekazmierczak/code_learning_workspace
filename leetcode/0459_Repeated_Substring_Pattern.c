/*
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

bool compare(char* s, int position, int len) {
    if (len % position) {
        return 0;
    }

    int i = 0;
    while (s[i] != '\0') {
        if (s[i] != s[i % position]) {
            return 0;
        }
        i++;
    }

    return 1;
}

bool repeatedSubstringPattern(char* s) {
    int len = -1;
    while (s[++len] != '\0');

    for (int i = 1; i < len / 2 + 1; i++) {
        if (compare(s, i, len)) {
            return 1;
        }
    }

    return 0;
}

int main() {
    char * s = "abcabcabcabc";

    bool res = repeatedSubstringPattern(s);

    printf("%d", res);

    return 0;
}