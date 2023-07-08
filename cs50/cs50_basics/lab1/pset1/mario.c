c#include <cs50.h>
#include <stdio.h>

int get_size(void);
void print_left(int size, int counter);
void print_right(int size, int counter);
int main(void)
{
    int size = get_size();
    int counter = 1;
    for (int i = 0; i < size; i++)
    {
        print_left(size, counter);
        printf("  ");
        print_right(size, counter);
        counter++;
    }
}

// Getting size
int get_size(void)
{
    int size;
    do
    {
        size = get_int("Size: ");
    }
    while (size < 1 || size > 8);
    return size;
}
// Printing left pyramid
void print_left(int size, int counter)
{
    for (int i = 0; i < size; i++)
    {
        if (counter < size)
        {
            printf(" ");
        }
        else
        {
            printf("#");
        }
        counter++;
    }
}
// Printing right pyramid
void print_right(int size, int counter)
{
    for (int i = 0; i < counter; i++)
    {
        printf("#");
    }
    printf("\n");
    counter++;
}