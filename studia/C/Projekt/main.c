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
    scanf_s("%i", &liczba_mieszkańców);

    printf("Podaj budżet początkowy: ");
    scanf_s("%i", &budżet);
    
    struct Miasteczko *miasteczko = stwórz_miasteczko(liczba_mieszkańców, budżet);

    menu(miasteczko);

    return EXIT_SUCCESS;
}