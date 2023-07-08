#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);
int a = 0;
int counter = 0;

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }
    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    //  TODO
    if (strlen(input) == 0)
    {
        return a;
    }
    else
    {
        a = a + (input[strlen(input) - 1] - 48) * pow(10, counter);
        input[strlen(input) - 1] = 0;
        counter++;
        convert(input);
        return a;
    }
}