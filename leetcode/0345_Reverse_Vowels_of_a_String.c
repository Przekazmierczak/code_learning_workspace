/*
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
*/

#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

char vowels[] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

bool checkIfVowel(char letter) {
    bool isVowel = false;
    for (int i = 0; i < 10; i++) {
        if (letter == vowels[i]) {
            return true;
        }
    }
    return false;
}

char* reverseVowels(char* s) {
    int len = 0;
    char temp;
    while (s[len] != '\0') {
        len += 1;
    }
    
    int l = 0;
    int r = len;
    
    while (1) {
        while (l < r && checkIfVowel(s[l]) == false) {
            l += 1;
        }
        
        while (l < r && checkIfVowel(s[r]) == false) {
            r -= 1;
        }
        
        if (l >= r) {
            break;
        }
        
        temp = s[l];
        s[l++] = s[r];
        s[r--] = temp;
    }
    
    return s;
}

int main() {
    char s[] = "IceCreAm";

    reverseVowels(s);

    printf("%s", s);

    return 0;
}