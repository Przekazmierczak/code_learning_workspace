/*
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int longestPalindrome(char* s) {
    int dict[52] = {0};
    int res = 0;

    int position = 0;
    while (s[position] != '\0') {
        if (s[position] < 97) {
            dict[s[position++] - 'A']++;
        } else {
            dict[s[position++] - 'a' + 26]++;
        }
    }

    bool ifOdd = false;
    for (int i = 0; i < 52; i++) {
        res += dict[i];
        if (dict[i] % 2) {
            if (!ifOdd) {
                ifOdd = true;
            } else {
                res -= 1;
            }
        }
    }

    return res;
}

int main() {
    char* s = "abccccdd";

    int res = longestPalindrome(s);

    printf("%d", res);

    return 0;
}