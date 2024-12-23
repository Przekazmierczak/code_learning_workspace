/*
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
*/

#include <stdio.h>

void reverseString(char* s, int sSize) {
    int p1 = 0;
    int p2 = sSize - 1;
    char temp;
    
    while (p1 < p2) {
        temp = s[p1];
        s[p1] = s[p2];
        s[p2] = temp;
        p1++;
        p2--;
    };
}

int main() {
    char s[] = {'h','e','l','l','o'};
    int sSize = 5;

    reverseString(s, sSize);

    for (int i = 0; i < sSize; i++) {
        printf("%c", s[i]);
    }
}