#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage: ./reverse input.wav output.wav\n");
        return 1;
    }
    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;

    fread(&header, sizeof(WAVHEADER), 1, input);
    {
        printf("size is: %i\n", header.chunkSize);
        printf("numChannels is: %i\n", header.numChannels);
        printf("blockAlign is: %i\n", header.blockAlign);
        printf("bitsPerSample is: %i\n", header.bitsPerSample);
    }
    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        // Open output file for writing
        // TODO #5
        FILE *output = fopen(argv[2], "w");
        if (output == NULL)
        {
            printf("Could not open file.\n");
            return 1;
        }
        // Write header to file
        // TODO #6

        const int HEADER_SIZE = 44;
        BYTE head[HEADER_SIZE];
        fwrite(&header, sizeof(BYTE), HEADER_SIZE, output);
        // Use get_block_size to calculate size of block
        // TODO #7
        WORD block_size = get_block_size(header);
        printf("block_size is: %i\n", block_size);
        // Write reversed audio to file
        // TODO #8
        int counter = 0;
        int sample_size = header.subchunk2Size;
        printf("header.subchunk2Size is: %i\n", sample_size);
        WORD* sample = malloc(sample_size);
        fseek(input, - block_size * sizeof(BYTE), SEEK_END);
        while (fread(sample, sizeof(BYTE), block_size, input) && ftell(input) > 44)
        {
            fwrite(sample, sizeof(BYTE), block_size, output);
            fseek(input, -2 * block_size * sizeof(BYTE), SEEK_CUR);
            printf("ftell is: %li\n", ftell(input));
            counter++;
        }
        printf("counter is: %i\n", counter);
        free(sample);
        fclose(input);
        fclose(output);
    }
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] == 87 && header.format[1] == 65 && header.format[2] == 86 && header.format[3] == 69)
    {
        printf("It is a WAV format\n");
        return 0;
    }
    printf("It is not a WAV format\n");
    return 1;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    WORD block_size = header.blockAlign;
    return block_size;
}