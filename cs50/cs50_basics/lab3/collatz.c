#include <cs50.h>
#include <stdio.h>

int counter[1] = {0};
int collatz(int n);

int main (void)
{
    // int counter[1] = {0};
    int n = get_int("Enter a number: ");
    collatz(n);
}

int collatz(int n)
{
    if (n == 1)
    {
        // printf("n = %i\n", n);
        printf("%i\n", counter[0]);
        return 1;
    }
    else
    {
        if (n % 2 == 0)
        {
            // printf("n = %i\n", n);
            counter[0]++;
            return collatz(n / 2);
        }
        else
        {
            // printf("n = %i\n", n);
            counter[0]++;
            return collatz(3 * n + 1);
        }
    }
}