#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "symulacja.h"

void menu(struct Miasteczko *miasteczko) {
    system("cls");
    printf("MENU\n");
    printf("Wybierz opcję:\n");
    printf("1. Symulacja\n");

    int opcja;
    int input = scanf_s("%i", &opcja);

    if (input != 1) {
        int c;
        while ((c = getchar()) != '\n' && c != EOF);
        menu(miasteczko);
    }

    switch (opcja) {
        case 1:
            symulacja(miasteczko);
        default:
            int c;
            while ((c = getchar()) != '\n' && c != EOF);
            menu(miasteczko);
    }
}