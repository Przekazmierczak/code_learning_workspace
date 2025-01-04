/*
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

bool isCapital(char l) {
    if (l >= 65 && l <= 90) {
        return true;
    }
    return false;
}

bool detectCapitalUse(char* word) {
    bool ifFirstCapital = false;
    
    if (isCapital(word[0])) {
        ifFirstCapital = true;
    }
    
    int i = 1;
    while (word[i] != '\0') {
        if (!ifFirstCapital && isCapital(word[i])) {
            return false;
        }
        
        if (ifFirstCapital && i >= 2 && isCapital(word[i]) != isCapital(word[i - 1])) {
            return false;
        }
        i++;
    }
    
    return true;
}

int main() {
    char* word = "USA";

    bool res = detectCapitalUse(word);

    printf("%d", res);

    return 0;
}