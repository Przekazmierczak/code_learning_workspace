#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string word = get_string("Player 1: ");

    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper((char)word[i]) != 0)
        {
            printf("%c\n", word[i]);
        }
        else
        {
            printf("%c\n", word[i] - 32);
        }
    }
}

