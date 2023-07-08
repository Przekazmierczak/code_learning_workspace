#include <stdio.h>
#include <cs50.h>

int main(void)
// {
//     for (int i = 0; i < 4; i++)
//     {
//         printf("?");
//     }
// printf("\n");
// }

{
    // Get size of grid
    int n;
    do
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    // Print grid of bricks

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}