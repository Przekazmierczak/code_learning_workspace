// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

//Counter
int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *ptr = table[hash(word)];
    while (ptr != NULL)
    if (strcasecmp(ptr->word, word) == 0)
    {
        return true;
    }
    else
    {
        ptr = ptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }
    char dword[LENGTH + 1];
    while(fscanf(file, "%s", dword) == 1)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, dword);
        n->next = NULL;
        if (table[hash(dword)] == NULL)
        {
            table[hash(dword)] = n;
        }
        else
        {
            n->next = table[hash(dword)];
            table[hash(dword)] = n;
        }
        counter++;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *tmp;
    for (int i = 0; i < 26; i++)
    {
        node *cursor = table[i];
        while(cursor != NULL)
        {
            tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
