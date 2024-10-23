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
    int ilość_pozycji = 10;
    struct Cmentarz *cmentarz = stwórz_cmentarz(ilość_pozycji);

    for (;;) {
        printf("----------------------------------------\n");
        postarzej_mieszkańców(miasteczko);
        śmierć_naturalna(miasteczko, cmentarz);
        dodaj_mieszkańca(miasteczko);
        lista_osób_na_cmenatrzu(cmentarz);
        informacje_o_mieszkańcach(miasteczko);
        Sleep(2000);
    }

    // uwolnij_mieszkańców(miasteczko);
    // free(miasteczko);

    return EXIT_SUCCESS;
}