#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string word = get_string("Enter your message: ");
    for (int i = 0; i < strlen(word); i++)
    {
        // printf("%i\n", word[i]);
        int string_char = word[i];
        for (int j = 7; j >= 0; j--)
        {
            if (string_char / (int)pow(2, j) == 1)
            {
                print_bulb(1);
                string_char = string_char - (int)pow(2, j);
            }
            else
            {
                print_bulb(0);
            }
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
