#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <windows.h>
#include <conio.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "smierc.h"
#include "budynki.h"
#include "symulacja.h"
#include "menu.h"

int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");
    srand(time(NULL));

    int liczba_mieszkańców;
    int budżet;
    system("cls");  // Wyczyść ekran (dla systemu Windows)
    printf("Witaj w symulacji miasta!\n");

    printf("Podaj początkową liczbę mieszkańców: ");
    int input_mieszkańcy = 0;
    while (input_mieszkańcy != 1) {
        input_mieszkańcy = scanf_s("%i", &liczba_mieszkańców);
        if (input_mieszkańcy != 1) {
            printf("Podaj początkową liczbę mieszkańców (w formacie liczbowym): ");
            int c;
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    printf("Podaj budżet początkowy: ");
    int input_budżet = 0;
    while (input_budżet != 1) {
        input_budżet = scanf_s("%i", &budżet);
        if (input_budżet != 1) {
            printf("Podaj budżet początkowy (w formacie liczbowym): ");
            int c;
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }
    
    struct Miasteczko *miasteczko = stwórz_miasteczko(liczba_mieszkańców, budżet);

    menu(miasteczko);

    return EXIT_SUCCESS;
}