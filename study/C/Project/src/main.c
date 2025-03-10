#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
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
    
    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    printf("Witaj w symulacji miasta!\n");

    // Poberz liczbę mieszkańców od użytkownika
    printf("Podaj początkową liczbę mieszkańców: ");
    int input_mieszkańcy = 0;
    while (input_mieszkańcy != 1) {
        input_mieszkańcy = scanf("%i", &liczba_mieszkańców);  // Odczytaj liczbę mieszkańców
        if (input_mieszkańcy != 1) {
            printf("Podaj początkową liczbę mieszkańców (w formacie liczbowym): ");
            int c;
            // Oczyść bufor wejściowy, aby uniknąć zapętlenia
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    // Pobierz początkowy budżet
    printf("Podaj budżet początkowy: ");
    int input_budżet = 0;
    while (input_budżet != 1) {
        input_budżet = scanf("%i", &budżet);  // Odczytaj budżet
        if (input_budżet != 1) {
            printf("Podaj budżet początkowy (w formacie liczbowym): ");
            int c;
            // Oczyść bufor wejściowy, aby uniknąć zapętlenia
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }
    
    // Stwórz strukturę Miasteczko z danymi użytkownika
    struct Miasteczko *miasteczko = stwórz_miasteczko(liczba_mieszkańców, budżet);

    // Wywołaj funkcję menu, aby pozwolić użytkownikowi na interakcję z symulacją
    menu(miasteczko);

    return EXIT_SUCCESS;  // Zakończ program
}