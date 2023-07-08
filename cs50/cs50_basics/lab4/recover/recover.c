#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char *argv[])
{
    typedef uint8_t BYTE;
    const int size = 512;
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }
    int counter = 0;
    char* name = malloc(8 * sizeof(char));
    BYTE* block = malloc(size * sizeof(BYTE));
    FILE* actual = malloc(sizeof(double));
    while(fread(block, sizeof(BYTE), size, file) == size)
    {
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] & 0xf0) == 0xe0)
        {
            counter++;
            if (counter == 1)
            {
                sprintf(name, "%03i.jpg", counter);
                FILE *pic = fopen(name, "w");
                if (pic == NULL)
                {
                    printf("Could not open file2.\n");
                    return 1;
                }
                fwrite(block, sizeof(BYTE), size, pic);
                actual = pic;
            }
            else
            {
                fclose(actual);
                sprintf(name, "%03i.jpg", counter);
                FILE *pic = fopen(name, "w");
                if (pic == NULL)
                {
                    printf("Could not open file2.\n");
                    return 1;
                }
                fwrite(block, sizeof(BYTE), size, pic);
                actual = pic;
            }
        }
        else
        {
            if (counter != 0)
            {
                fwrite(block, sizeof(BYTE), size, actual);
            }
        }
    }
    free(name);
    free(block);
    free(actual);
    fclose(file);
    fclose(actual);
}