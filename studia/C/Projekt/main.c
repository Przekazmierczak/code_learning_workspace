#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <windows.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "smierc.h"
#include "budynki.h"

int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");
    srand(time(NULL));

    struct Miasteczko *miasteczko = stwórz_miasteczko();
    // Dodaj 100 początkowych mieszkańców do miasteczka
    for (int i = 0; i < 100; i++) {
        dodaj_mieszkańca(miasteczko, false);
    }

    int następny_budynek_w_planie = rand() % 3;
    // Główna pętla symulacji
    for (;;) {
        system("cls"); // Wyczyść ekran (dla systemu Windows)
        printf("----------------Rok:%i----------------------\n",miasteczko->rok);

        // Wyświetl informację o cmentarzu
        printf("----------------Cmentarz----------------------\n");
        if (miasteczko->cmentarz->ilość_rzędów <= 6) {
            lista_osób_na_cmenatrzu(miasteczko->cmentarz);
        } else {
            printf("Ilość rzędów: %i, ilość pozycji: %i\n", miasteczko->cmentarz->ilość_rzędów, miasteczko->cmentarz->ilość_pozycji);
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
        printf("Budżet: %lli\n", miasteczko->budżet);

        następny_budynek_w_planie = wybuduj_budynek(miasteczko, następny_budynek_w_planie);
        utrzymanie_budynków(miasteczko);

        bool pożar = (rand() % 25 == 0);
        if (pożar) printf("******************POŻAR***********************\n");
        bool powódź = (rand() % 25 == 0);
        if (powódź) printf("*****************POWÓDŹ**********************\n");
        bool trzęsienie_ziemi = (rand() % 25 == 0);
        if (trzęsienie_ziemi) printf("************TRZĘSIENIE ZIEMI*****************\n");

        // Sprawdź, czy któryś z mieszkańców umarł, jeżeli tak, usuń go z listy mieszkańców i dodaj na cmentarz
        śmierć_mieszkańców(miasteczko, miasteczko->cmentarz, pożar, powódź, trzęsienie_ziemi);
        // Dodaj nowych mieszkańców do miasteczka, liczba nowych osób zależy od liczby aktualnych mieszkańców
        for (int i = 0; i < (int)(((miasteczko->ilość_mieszkańców) / 50) * szpital(miasteczko->ilość_mieszkańców / miasteczko->szpitale)) + 1; i++) {
            dodaj_mieszkańca(miasteczko, true);
        }

        printf("Ilość szpitali: %i\n", miasteczko->szpitale);
        printf("Ilość budynków straży pożarnej: %i\n", miasteczko->straż_pożarna);
        printf("Ilość budynków szkolnych: %i\n", miasteczko->szkoły);
        printf("Stosunek %i", miasteczko->ilość_mieszkańców / miasteczko->szpitale);
        printf("Następny budynek %i", następny_budynek_w_planie);

        Sleep(300);
    }

    return EXIT_SUCCESS;
}