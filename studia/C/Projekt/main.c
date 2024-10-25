#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <windows.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"

int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");
    srand(time(NULL));

    struct Miasteczko *miasteczko = stwórz_miasteczko();
    // Dodaj 10 początkowych mieszkańców do miasteczka
    for (int i = 0; i < 10; i++) {
        dodaj_mieszkańca(miasteczko, false);
    }

    int ilość_pozycji = 10;
    struct Cmentarz *cmentarz = stwórz_cmentarz(ilość_pozycji);

    // Główna pętla symulacji
    for (;;) {
        system("cls"); // Wyczyść ekran (dla systemu Windows)
        printf("----------------Rok:%i----------------------\n",miasteczko->rok);

        // Wyświetl informację o cmentarzu
        printf("----------------Cmentarz----------------------\n");
        if (miasteczko->ilość_mieszkańców <= 250) {
            lista_osób_na_cmenatrzu(cmentarz);
        } else {
            printf("Ilość rzędów: %i, ilość pozycji: %i\n", cmentarz->ilość_rzędów, cmentarz->ilość_pozycji);
        }

        // Wyświetl informację o mieszkańcach
        printf("---------------Mieszkańcy---------------------\n");
        if (miasteczko->ilość_mieszkańców <= 60) {
            informacje_o_mieszkańcach(miasteczko);
        } else {
            printf("Ilość mieszkańców: %i\n", miasteczko->ilość_mieszkańców);
        }

        // Zwiększ wiek wszystkich mieszkańców
        postarzej_mieszkańców(miasteczko);
        // Sprawdź, czy któryś z mieszkańców umarł, jeżeli tak, usuń go z listy mieszkańców i dodaj na cmentarz
        śmierć_naturalna(miasteczko, cmentarz);
        // Dodaj nowych mieszkańców do miasteczka, liczba nowych osób zależy od liczby aktualnych mieszkańców
        for (int i = 0; i < (miasteczko->ilość_mieszkańców) / 50 + 1; i++) {
            dodaj_mieszkańca(miasteczko, true);
        }
        Sleep(1000);

    }

    return EXIT_SUCCESS;
}