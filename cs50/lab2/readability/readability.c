#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    count_letters(text);
    // printf("%i letters\n", count_letters(text));
    count_words(text);
    // printf("%i words\n", count_words(text));
    count_sentences(text);
    // printf("%i sentences\n", count_sentences(text));

    float L = (float)count_letters(text) / (float)count_words(text) * 100;
    // printf("L %f\n", L);
    float S = (float)count_sentences(text) / (float)count_words(text) * 100;
    // printf("S %f\n", S);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded_index = round(index);
    if (rounded_index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (rounded_index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rounded_index);
    }
}

int count_letters(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isupper(text[i]) != 0)
        {
            counter++;
        }
        else if (islower(text[i]) != 0)
        {
            counter++;
        }
    }
    return counter;
}

int count_words(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 32)
        counter++;
    }
    counter++;
    return counter;
}

int count_sentences(string text)
{
    int counter = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        counter++;
    }
    return counter;
}