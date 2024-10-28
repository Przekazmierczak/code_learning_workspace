#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "cmentarz.h"

struct Cmentarz* stwórz_cmentarz(int ilość_pozycji) {
    struct Cmentarz *cmentarz = malloc(sizeof(struct Cmentarz));
    cmentarz->ilość_pozycji = ilość_pozycji;
    cmentarz->ilość_rzędów = 1;

    // Alokuj pamięci dla wskaźnika na tablicę rzędów
    cmentarz->aleja = malloc(sizeof(struct Grób**));
    if (cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja w stwórz_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    // Alokuj pamięć dla pierwszego rzędu na cmentarzu
    cmentarz->aleja[0] = malloc(ilość_pozycji * sizeof(struct Grób*));
    if (cmentarz->aleja[0] == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[0] w stwórz_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    // Inicjalizuj miejsca na groby jako NULL
    for (int i = 0; i < ilość_pozycji; i++) {
        cmentarz->aleja[0][i] = NULL;
    }
    return cmentarz;
};

void powiększ_cmentarz(struct Cmentarz *cmentarz) {
    cmentarz->ilość_rzędów += 1;

    // Realokuj pamięć dla wskaźnika na tablicę rzędów
    cmentarz->aleja = realloc(cmentarz->aleja, cmentarz->ilość_rzędów * sizeof(struct Grób**));
    if (cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja w powiększ_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    // Alokuj pamięĆ dla nowego rzędu
    cmentarz->aleja[cmentarz->ilość_rzędów - 1] = malloc(cmentarz->ilość_pozycji * sizeof(struct Grób*));
    if (cmentarz->aleja[cmentarz->ilość_rzędów - 1] == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[cmentarz->ilość_rzędów - 1] w powiększ_cmentarz.\n");
        exit(EXIT_FAILURE);
    }

    // Inicjalizuj miejsca na groby w nowym rzędzie jako NULL
    for (int i = 0; i < cmentarz->ilość_pozycji; i++) {
        cmentarz->aleja[cmentarz->ilość_rzędów - 1][i] = NULL;
    }
}

void dodaj_zmarłego(struct Cmentarz *cmentarz, struct Mieszkaniec *mieszkaniec, int rok_śmierci, int rząd_startowy) {
    int i = rząd_startowy;
    for (; i < cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < cmentarz->ilość_pozycji; j++) {
            // Sprawdź, czy miejsce jest puste lub czy grób kwalifikuje się do likwidacji
            if (cmentarz->aleja[i][j] == NULL || cmentarz->aleja[i][j]->rok_likwidacji < rok_śmierci) {
                // Jeśli miejsce jest wolne, alokuj pamięć dla nowego grobu
                if (cmentarz->aleja[i][j] == NULL) {
                    cmentarz->aleja[i][j] = malloc(sizeof(struct Grób));
                    if (cmentarz->aleja[i][j] == NULL) {
                        printf("Błąd: Nie udało się przydzielić pamięci dla cmentarz->aleja[i][j] w dodaj_zmarłego.\n");
                        exit(EXIT_FAILURE);
                    }
                // Jeśli grób jest już zajęty, uwalnij pamięć poprzedniego zmarłego
                } else {
                    uwolnij_mieszkańca(cmentarz->aleja[i][j]->zmarły);
                }
                // Umieść nowego zmarłego i oblicz roku likwidacji grobu
                cmentarz->aleja[i][j]->zmarły = mieszkaniec;
                cmentarz->aleja[i][j]->rok_likwidacji = określ_rok_likwidacji(mieszkaniec, rok_śmierci);
                return;
            }
        }
    }
    // Jeśli nie znaleziono miejsca, powiększ cmentarz i dodaJ zmarłego do nowego rzędu
    powiększ_cmentarz(cmentarz);
    dodaj_zmarłego(cmentarz, mieszkaniec, rok_śmierci, cmentarz->ilość_rzędów - 1);
}

int określ_rok_likwidacji(struct Mieszkaniec *mieszkaniec, int rok_śmierci) {
    // Oblicz rok likwidacji grobu na podstawie pensji zmarłego
    if (mieszkaniec->pensja > 13000) {
        return rok_śmierci + 100;
    } else if (mieszkaniec->pensja > 11000) {
        return rok_śmierci + 80;
    } else if (mieszkaniec->pensja > 9000) {
        return rok_śmierci + 60;
    } else if (mieszkaniec->pensja > 7000) {
        return rok_śmierci + 40;
    }
    return rok_śmierci + 20;
}

void lista_osób_na_cmenatrzu(struct Cmentarz *cmentarz) {
    for (int i = 0; i < cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < cmentarz->ilość_pozycji; j++) {
            printf("W rzędzie nr %i w miejscu nr %i spoczywa: ", i, j);
            if (cmentarz->aleja[i][j] != NULL) {
                // Wyświetl dane o zmarłym, jeśli grób jest zajęty
                printf("%s %s ", cmentarz->aleja[i][j]->zmarły->imię, cmentarz->aleja[i][j]->zmarły->nazwisko);
                printf("Rok likwidacji: %i\n", cmentarz->aleja[i][j]->rok_likwidacji);
            } else {
                // Wyświetl informacje, że miejsce jest puste
                printf("%s\n", "Miejsce jest aktualnie puste");
            }
        }
    }
}