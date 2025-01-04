/*
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:

1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

void reverse(char* s, int p1, int p2) {
    char temp;
    while (p1 < p2) {
        temp = s[p1];
        s[p1] = s[p2];
        s[p2] = temp;
        p1++;
        p2--;
    }
}

char* reverseStr(char* s, int k) {
    int len = -1;
    while (s[++len] != '\0');

    int p1 = 0;
    int p2 = k - 1;
    
    while (p2 < len) {
        reverse(s, p1, p2);
        p1 += 2*k;
        p2 += 2*k;
    }

    if (p1 < len - 1) {
        reverse(s, p1, len -1);
    }

    return s;
}

int main() {
    char s[] = "abcdefg";
    int k = 2;

    char* res = reverseStr(s, k);

    printf("%s", res);

    return 0;
}