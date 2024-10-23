#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "cmentarz.h"

struct Cmentarz* stwórz_cmentarz(int ilość_pozycji) {
    struct Cmentarz *cmentarz = malloc(sizeof(struct Cmentarz));
    cmentarz->ilość_pozycji = ilość_pozycji;
    cmentarz->ilość_rzędów = 1;

    cmentarz->aleja = malloc(sizeof(struct Grób**));
    if (cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja w stwórz_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    cmentarz->aleja[0] = malloc(ilość_pozycji * sizeof(struct Grób*));
    if (cmentarz->aleja[0] == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[0] w stwórz_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < ilość_pozycji; i++) {
        cmentarz->aleja[0][i] = NULL;
    }
    return cmentarz;
};

void powiększ_cmentarz(struct Cmentarz *cmentarz) {
    cmentarz->ilość_rzędów += 1;

    cmentarz->aleja = realloc(cmentarz->aleja, cmentarz->ilość_rzędów * sizeof(struct Grób**));
    if (cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja w powiększ_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    cmentarz->aleja[cmentarz->ilość_rzędów - 1] = malloc(cmentarz->ilość_pozycji * sizeof(struct Grób*));
    if (cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[cmentarz->ilość_rzędów - 1] w powiększ_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

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
                if (cmentarz->aleja[i][j] == NULL) {
                    printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[i][j] w dodaj_zmarłego.\n");
                    exit(EXIT_FAILURE);
                }

                cmentarz->aleja[i][j]->zmarły = mieszkaniec;
                cmentarz->aleja[i][j]->rok_likwidacji = 0;
                return;
            }
        }
    }
    powiększ_cmentarz(cmentarz);
    dodaj_zmarłego(cmentarz, mieszkaniec, cmentarz->ilość_rzędów - 1);
}

void lista_osób_na_cmenatrzu(struct Cmentarz *cmentarz) {
    for (int i = 0; i < cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < cmentarz->ilość_pozycji; j++) {
            printf("W rzędzie nr %i w miejscu nr %i spoczywa: ", i, j);
            if (cmentarz->aleja[i][j] != NULL) {
                printf("%s %s\n", cmentarz->aleja[i][j]->zmarły->imię, cmentarz->aleja[i][j]->zmarły->nazwisko);
            } else {
                printf("%s\n", "Miejsce jest aktualnie puste");
            }
        }
    }
}