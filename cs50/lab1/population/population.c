#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startingSize;
    do
    {
        startingSize = get_int("Enter starting population size: ");
    }
    while (startingSize < 9);

    // TODO: Prompt for end size
    int endingSize;
    do
    {
        endingSize = get_int("Enter ending population size: ");
    }
    while (endingSize < startingSize);

    // TODO: Calculate number of years until we reach threshold
    int n = 0;
    while (startingSize < endingSize)
    {
        int oneYear = startingSize + (startingSize / 3) - (startingSize / 4);
        startingSize = oneYear;
        n++;
        // printf("%i\n", startingSize);
        // printf("%i\n", n);
    }
    // TODO: Print number of years
    printf("Years: %i\n", n);
}
