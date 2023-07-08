#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
    }
    else
    {
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: " );
        for (int i = 0; i < strlen(plaintext); i++)
        {
            if (plaintext[i] >= 65 && plaintext[i] <= 90)
            {
                int cipherchar = plaintext[i] + atoi(argv[1]) % 26;
                if (cipherchar <= 90)
                {
                    printf("%C", cipherchar);
                }
                else
                {
                    printf("%C", cipherchar - 26);
                }
            }
            else if (plaintext[i] >= 97 && plaintext[i] <= 122)
            {
                int cipherchar = plaintext[i] + atoi(argv[1]) % 26;
                if (cipherchar <= 122)
                {
                    printf("%C", cipherchar);
                }
                else
                {
                    printf("%C", cipherchar - 26);
                }
            }
            else
            {
                printf("%C", plaintext[i]);
            }
        }
    }
    printf("\n");
}