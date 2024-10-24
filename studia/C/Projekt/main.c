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
    for (int i = 0; i < 10; i++) {
        dodaj_mieszkańca(miasteczko, false);
    }

    int ilość_pozycji = 10;
    struct Cmentarz *cmentarz = stwórz_cmentarz(ilość_pozycji);

    for (;;) {
        system("cls");
        printf("----------------Rok:%i----------------------\n",miasteczko->rok);

        printf("----------------Cmentarz----------------------\n");
        if (miasteczko->ilość_mieszkańców <= 250) {
            lista_osób_na_cmenatrzu(cmentarz);
        } else {
            printf("Ilość rzędów: %i, ilość pozycji: %i\n", cmentarz->ilość_rzędów, cmentarz->ilość_pozycji);
        }

        printf("---------------Mieszkańcy---------------------\n");
        if (miasteczko->ilość_mieszkańców <= 60) {
            informacje_o_mieszkańcach(miasteczko);
        } else {
            printf("Ilość mieszkańców: %i\n", miasteczko->ilość_mieszkańców);
        }

        postarzej_mieszkańców(miasteczko);
        śmierć_naturalna(miasteczko, cmentarz);
        for (int i = 0; i < (miasteczko->ilość_mieszkańców) / 50 + 1; i++) {
            dodaj_mieszkańca(miasteczko, true);
        }
        Sleep(300);

    }

    // uwolnij_mieszkańców(miasteczko);
    // free(miasteczko);

    return EXIT_SUCCESS;
}