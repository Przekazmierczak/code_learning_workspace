/*
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Explanation:
Both "a" and "A" are in the 2nd row of the American keyboard due to case insensitivity.

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char toLower(char letter) {
    if (letter >= 65 && letter <= 90) {
        letter += 32;
    }
    return letter;
}

bool checkOneLine(char* word, char* line) {
    int i = 1;
    int j;
    char curr;
    bool ifInLine;
    while (word[i] != '\0') {
        j = 0;
        ifInLine = false;
        curr = toLower(word[i]);
        while(line[j] != '\0') {
            if (line[j] == curr) {
                ifInLine = true;
                break;
            }
            j++;
        }
        if (!ifInLine) {
            return false;
        }
        i++;
    }
    return true;
}

char* possibleLine(char firstLetter, char* line1, char* line2, char* line3) {
    for (int i = 0; i < 10; i++) {
        if (firstLetter == line1[i]) {
            return line1;
        }
    }
    for (int i = 0; i < 9; i++) {
        if (firstLetter == line2[i]) {
            return line2;
        }
    }
    for (int i = 0; i < 7; i++) {
        if (firstLetter == line3[i]) {
            return line3;
        }
    }
    return line1;
}


char** findWords(char** words, int wordsSize, int* returnSize) {
    char** res = malloc(100* sizeof(char*));
    *returnSize = 0;
    char* line1 = "qwertyuiop";
    char* line2 = "asdfghjkl";
    char* line3 = "zxcvbnm";
    char* currLine;
    char firstLetter;
    bool ifOneLine;

    for (int i = 0; i < wordsSize; i++) {
        firstLetter = toLower(words[i][0]);

        currLine = possibleLine(firstLetter, line1, line2, line3);
        if (checkOneLine(words[i], currLine)) {
            res[*returnSize] = words[i];
            (*returnSize)++;
        }
    }

    return res;
}

int main() {
    int wordsSize = 4;
    char* words[] = {"Hello", "Alaska", "Dad", "Peace"};
    char** res;
    int* returnSize = malloc(sizeof(int));

    res = findWords(words, wordsSize, returnSize);

    for (int i = 0; i < *returnSize; i++) {
        printf("%s\n", res[i]);
    }

    return 0;
}