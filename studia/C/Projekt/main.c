#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include "mieszkaniec.h"
#include "miasteczko.h"

int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");
    srand(time(NULL));

    struct Miasteczko *miasteczko = stwórz_miasteczko();

    for (int i = 0; i < 10; i++) {
        dodaj_mieszkańca(miasteczko);
    }

    informacje_o_mieszkańcach(miasteczko);

    uwolnij_mieszkańców(miasteczko);
    free(miasteczko);

    return EXIT_SUCCESS;
}