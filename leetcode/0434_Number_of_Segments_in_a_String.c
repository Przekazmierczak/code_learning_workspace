/*
Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1

Constraints:
0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

int countSegments(char* s) {
    int segments = 0;
    int ifSpace = 1;
    int i = 0;
    while (s[i] != '\0') {
        if (s[i] != ' ' && ifSpace) {
            ifSpace = 0;
            segments++;
        } else if (s[i] == ' ' && !ifSpace) {
            ifSpace = 1;
        }
        i++;
    }
    return segments;
}

int main() {
    char * s = "Hello, my name is John";

    int res = countSegments(s);

    printf("%d", res);

    return 0;
}