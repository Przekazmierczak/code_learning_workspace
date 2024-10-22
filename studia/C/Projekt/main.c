#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include "mieszkaniec.h"
#include "miasteczko.h"

struct Cmentarz {
    int ilość_pozycji;
    int ilość_rzędów;
    struct Grób ***aleja;
};

struct Grób {
    struct Mieszkaniec *zmarły;
    int rok_likwidacji;
};

struct Cmentarz* stwórz_cmentarz(int ilość_pozycji) {
    struct Cmentarz *cmentarz = malloc(sizeof(struct Cmentarz));
    cmentarz->ilość_pozycji = ilość_pozycji;
    cmentarz->ilość_rzędów = 1;
    cmentarz->aleja = malloc(sizeof(struct Grób**));
    cmentarz->aleja[0] = malloc(ilość_pozycji * sizeof(struct Grób*));
    for (int i = 0; i < ilość_pozycji; i++) {
        cmentarz->aleja[0][i] = NULL;
    }
    return cmentarz;
};

void powiększ_cmentarz(struct Cmentarz *cmentarz) {
    cmentarz->ilość_rzędów += 1;
    cmentarz->aleja = realloc(cmentarz->aleja, cmentarz->ilość_rzędów * sizeof(struct Grób**));
    cmentarz->aleja[cmentarz->ilość_rzędów - 1] = malloc(cmentarz->ilość_pozycji * sizeof(struct Grób*));
    for (int i = 0; i < cmentarz->ilość_pozycji; i++) {
        cmentarz->aleja[cmentarz->ilość_rzędów - 1][i] = NULL;
    }
}

void dodaj_zmarłego(struct Cmentarz *cmentarz, struct Mieszkaniec *mieszkaniec, int rząd_startowy) {
    int i = rząd_startowy;
    for (; i < cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < cmentarz->ilość_pozycji; j++) {
            if (cmentarz->aleja[i][j] == NULL) {
                cmentarz->aleja[i][j] = malloc(sizeof(struct Grób));
                cmentarz->aleja[i][j]->zmarły = malloc(sizeof(struct Mieszkaniec));
                cmentarz->aleja[i][j]->zmarły = mieszkaniec;
                cmentarz->aleja[i][j]->rok_likwidacji = 0;
                return;
            }
        }
    }
    powiększ_cmentarz(cmentarz);
    dodaj_zmarłego(cmentarz, mieszkaniec, cmentarz->ilość_rzędów - 1);
}

int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");
    srand(time(NULL));

    struct Miasteczko *miasteczko = stwórz_miasteczko();

    for (int i = 0; i < 55; i++) {
        dodaj_mieszkańca(miasteczko);
    }

    int ilość_pozycji = 10;
    struct Cmentarz *cmentarz = stwórz_cmentarz(ilość_pozycji);

    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    int counter = 0;
    int counter2 = 0;

    for (int i = 0; i < 52; i++) {
        printf("%i\n", counter++);
        dodaj_zmarłego(cmentarz, aktualny_mieszkaniec->val, 0);
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }

    for (int i = 0; i < cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < cmentarz->ilość_pozycji; j++) {
            printf("%i", counter2++);
            if (cmentarz->aleja[i][j] != NULL) {
                printf("%s\n", cmentarz->aleja[i][j]->zmarły->imię);
            } else {
                printf("%s\n", "NULL");
            }
        }
    }

    // informacje_o_mieszkańcach(miasteczko);

    // uwolnij_mieszkańców(miasteczko);
    // free(miasteczko);

    return EXIT_SUCCESS;
}