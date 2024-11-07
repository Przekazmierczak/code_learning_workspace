#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mieszkaniec.h"

const int ILOŚĆ_KATEGORII = 4;
const int ILOŚĆ_IMION_NAZWISK = 40;
const int MAX_IMIĘ_NAZWISKO = 20;

char*** wczytaj_listę_imion_z_pliku() {
    // Stwórz tabelę do przechowania możliwych imion oraz nazwisk
    char ***lista_możliwych_imion = malloc(ILOŚĆ_KATEGORII * sizeof(char**));
    for (int i = 0; i < 4; i++) {
        lista_możliwych_imion[i] = malloc(ILOŚĆ_IMION_NAZWISK * sizeof(char*));
        for (int j = 0; j < 40; j++) {
            lista_możliwych_imion[i][j] = malloc(MAX_IMIĘ_NAZWISKO * sizeof(char));
        }
    }
    
    char buffer[10000]; // Bufor do odczytu linii z pliku
    int linia = 0;

    FILE *file = fopen("imiona.txt", "r");

    if (file == NULL) {
        printf("Błąd: Nie udało otworzyć się pliku imiona.txt\n");
        exit(EXIT_FAILURE);
    } else {
        // Odczytaj plik linia po linii
        while (!feof(file) && !ferror(file)) {
            if (fgets(buffer, 10000, file) != NULL) {
                int litera_linia = 0;
                int litera_imię = 0;
                int imię = 0;
                // Przejdź po wszystkich literach w danej linii
                while (buffer[litera_linia] != '\0') {
                    if (buffer[litera_linia] != ' ' && buffer[litera_linia] != '\n') {
                        lista_możliwych_imion[linia][imię][litera_imię] = buffer[litera_linia];
                        litera_imię++;
                    } else {
                        lista_możliwych_imion[linia][imię][litera_imię] = '\0';  // Zakończy imię/nazwisko
                        imię ++;  // Przejdź do kolejnego imienia/nazwiska
                        litera_imię = 0;
                    }
                    litera_linia++;
                }
                linia++;  // Przejdź do następnej linii
            }
        }
    }

    fclose(file);
    return lista_możliwych_imion;
}

struct Mieszkaniec* stwórz_mieszkańca(bool noworodek, char*** lista_możliwych_imion) {
    struct Mieszkaniec* mieszkaniec = malloc(sizeof(struct Mieszkaniec));
    if (mieszkaniec == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla struktury mieszkaniecw stwórz_mieszkańca.\n");
        exit(EXIT_FAILURE);
    }

    // Losuj płeć mieszkańca
    mieszkaniec->płeć = rand() % 2 ? Mężczyzna : Kobieta;

    // Przydziel imię i nazwisko w zależności od płci
    if (mieszkaniec->płeć == Mężczyzna) {
        char* imię = lista_możliwych_imion[0][rand() % 40];
        mieszkaniec->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (mieszkaniec->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->imię w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->imię, imię);
    
        char* nazwisko = lista_możliwych_imion[2][rand() % 40];
        mieszkaniec->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (mieszkaniec->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->nazwisko w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->nazwisko, nazwisko);
    } else {
        char* imię = lista_możliwych_imion[1][rand() % 40];
        mieszkaniec->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (mieszkaniec->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->imię w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->imię, imię);

        char* nazwisko = lista_możliwych_imion[3][rand() % 40];
        mieszkaniec->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (mieszkaniec->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->nazwisko w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->nazwisko, nazwisko);
    }

    // Ustaw wiek i pensję mieszkańca w zależności od tego, czy jest noworodkiem
    if (noworodek) {
        mieszkaniec->wiek = 0;
        mieszkaniec->pensja = 0;
    } else {
        mieszkaniec->wiek = rand() % 70;
        mieszkaniec->pensja = 0;
        // W przypadku w którym mieszkaniec ma co najmniej 18 lat, losuj czy posiada pracę
        if (mieszkaniec->wiek >= 18) {
            int i = mieszkaniec->wiek - 18;
            while (i >= 0 && mieszkaniec->pensja == 0) {
                praca(mieszkaniec);
                i--;
            }
        }
    }
    return mieszkaniec;
}

// Spróbuj przydzielić pracę mieszkańcowi, oraz ustawial losową pensję
void praca(struct Mieszkaniec* mieszkaniec) {
    if (rand() % 5 == 0) mieszkaniec->pensja = 5000 + (rand() % 10000);
}

void uwolnij_mieszkańca(struct Mieszkaniec* mieszkaniec) {
    free(mieszkaniec->imię);
    free(mieszkaniec->nazwisko);
    free(mieszkaniec);
}