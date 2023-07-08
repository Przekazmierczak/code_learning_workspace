#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // Check for command line args
    if (argc != 2)
    {
        printf("Usage: ./read infile\n");
        return 1;
    }

    // Create buffer to read into
    char buffer[7];

    // Create array to store plate numbers
    char *plates = malloc(7 * 8);

    FILE *infile = fopen(argv[1], "r");

    int idx = 0;

    while (fread(buffer, 1, 7, infile) == 7)
    {
        // Replace '\n' with '\0'
        buffer[6] = '\0';

        // Save plate number in array
        strcpy(&plates[idx], buffer);
        idx = idx + 7;
    }

    for (int i = 0; i < 7 * 8; i = i + 7)
    {
        // printf("%s\n", plates[idx]);
        printf("%s\n", plates + i);
    }
    fclose(infile);
    free(plates);
}
