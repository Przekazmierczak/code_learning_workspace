#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int check_if_correct(int argc, string argv);
void get_cipher(string key, string plaintext);
string key_to_upper (string key);


int main(int argc, string argv[])
{
    check_if_correct(argc, argv[1]);
    key_to_upper(argv[1]);
    if (check_if_correct(argc, argv[1]) == 1)
    {
        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");
        get_cipher(argv[1], plaintext);
    }
}

int check_if_correct(int argc, string argv)
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 0;
    }
    else if (strlen(argv) != 26)
    {
        printf("Key must contain 26 characters.");
        return 0;
    }
    return 1;
}

void get_cipher(string key, string plaintext)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isupper(plaintext[i]) > 0)
        {
           int cipherchar = plaintext[i] - 65;
           cipherchar = key[cipherchar];
           printf("%c", cipherchar);
        }
        else if (islower(plaintext[i]) > 0)
        {
           int cipherchar = plaintext[i] - 97;
           cipherchar = key[cipherchar];
           cipherchar = cipherchar + 32;
           printf("%c", cipherchar);
        }
        else
        {
           int cipherchar = plaintext[i];
           printf("%c", cipherchar);
        }
    }
    printf("\n");
}

string key_to_upper (string key)
{
    for (int i = 0; i <strlen(key); i++)
    if (islower(key[i]) > 0)
    {
        key[i] = key[i] - 32;
    }
    return key;
}