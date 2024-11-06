#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

#include "mieszkaniec.h"
#include "miasteczko.h"

#define MAX_IMIĘ_NAZWISKO 20

void zapisz_do_pliku(struct Miasteczko *miasteczko) {
    FILE *file = fopen("zapis.bin", "wb");

    if (!file){
        printf("Nie udało się utworzyć pliku do zapisu");
        exit(EXIT_FAILURE);
    }

    fwrite(&miasteczko->ilość_mieszkańców, sizeof(int), 1, file);
    fwrite(&miasteczko->rok, sizeof(int), 1, file);
    fwrite(&miasteczko->budżet, sizeof(long long), 1, file);

    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    for (int i = 0; i < miasteczko->ilość_mieszkańców; i++) {
        fwrite(aktualny_mieszkaniec->val->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        fwrite(aktualny_mieszkaniec->val->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        fwrite(&(aktualny_mieszkaniec->val->płeć), sizeof(char), 1, file);
        fwrite(&(aktualny_mieszkaniec->val->wiek), sizeof(int), 1, file);
        fwrite(&(aktualny_mieszkaniec->val->pensja), sizeof(int), 1, file);
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }

    fwrite(&miasteczko->cmentarz->ilość_pozycji,sizeof(int), 1, file);
    fwrite(&miasteczko->cmentarz->ilość_rzędów, sizeof(int), 1, file);

    bool pusta_pozycja;

    for (int i = 0; i < miasteczko->cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < miasteczko->cmentarz->ilość_pozycji; j++) {
            if (miasteczko->cmentarz->aleja[i][j] != NULL) {
                pusta_pozycja = false;
                fwrite(&(pusta_pozycja), sizeof(bool), 1, file);

                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->płeć), sizeof(char), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->wiek), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->pensja), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->rok_likwidacji), sizeof(int), 1, file);
            } else {
                pusta_pozycja = true;
                fwrite(&(pusta_pozycja), sizeof(bool), 1, file);
            }
        }
    }

    fwrite(&miasteczko->szpitale, sizeof(int), 1, file);
    fwrite(&miasteczko->straż_pożarna, sizeof(int), 1, file);
    fwrite(&miasteczko->szkoły, sizeof(int), 1, file);

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 40; j++) {
            fwrite(miasteczko->lista_możliwych_imion[i][j], sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        }
    }

    fclose(file);

}

void wczytaj_z_pliku(struct Miasteczko *miasteczko) {
    FILE *file = fopen("zapis.bin", "rb");

    if (!file){
        printf("Nie udało się otworzyć pliku do odczytu");
        exit(EXIT_FAILURE);
    }

    fread(&miasteczko->ilość_mieszkańców, sizeof(int), 1, file);
    fread(&miasteczko->rok, sizeof(int), 1, file);
    fread(&miasteczko->budżet, sizeof(long long), 1, file);

    miasteczko->mieszkańcy = NULL;

    struct Mieszkańcy *aktualny = NULL;
    struct Mieszkańcy **następny = &miasteczko->mieszkańcy;

    for (int i = 0; i < miasteczko->ilość_mieszkańców; i++) {
        aktualny = malloc(sizeof(struct Mieszkańcy));
        if (aktualny == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        aktualny->val = malloc(sizeof(struct Mieszkaniec));
        if (aktualny->val == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }

        aktualny->val->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (aktualny->val->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        fread(aktualny->val->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

        aktualny->val->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (aktualny->val->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        fread(aktualny->val->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

        fread(&(aktualny->val->płeć), sizeof(char), 1, file);
        fread(&(aktualny->val->wiek), sizeof(int), 1, file);
        fread(&(aktualny->val->pensja), sizeof(int), 1, file);

        *następny = aktualny;
        następny = &aktualny->next;
    }

    *następny = NULL;

    fread(&miasteczko->cmentarz->ilość_pozycji,sizeof(int), 1, file);
    fread(&miasteczko->cmentarz->ilość_rzędów, sizeof(int), 1, file);

    miasteczko->cmentarz->aleja = NULL;

    miasteczko->cmentarz->aleja = malloc(miasteczko->cmentarz->ilość_rzędów * sizeof(struct Grób**));

    bool pusta_pozycja;

    for (int i = 0; i < miasteczko->cmentarz->ilość_rzędów; i++) {
        miasteczko->cmentarz->aleja[i] = malloc(miasteczko->cmentarz->ilość_pozycji * sizeof(struct Grób*));
        for (int j = 0; j < miasteczko->cmentarz->ilość_pozycji; j++) {
            fread(&pusta_pozycja, sizeof(bool), 1, file);
            if (pusta_pozycja == false) {
                miasteczko->cmentarz->aleja[i][j] = malloc(sizeof(struct Grób));
                if (miasteczko->cmentarz->aleja[i][j] == NULL) {
                    printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }

                miasteczko->cmentarz->aleja[i][j]->zmarły = malloc(sizeof(struct Mieszkaniec));
                if (miasteczko->cmentarz->aleja[i][j]->zmarły == NULL) {
                    printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }

                miasteczko->cmentarz->aleja[i][j]->zmarły->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
                if (miasteczko->cmentarz->aleja[i][j]->zmarły->imię == NULL) {
                    printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }
                fread(miasteczko->cmentarz->aleja[i][j]->zmarły->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

                miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
                if (miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko == NULL) {
                    printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }
                fread(miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->płeć), sizeof(char), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->wiek), sizeof(int), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->pensja), sizeof(int), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->rok_likwidacji), sizeof(int), 1, file);
            } else {
                miasteczko->cmentarz->aleja[i][j] = NULL;
            }
        }
    }

    fread(&miasteczko->szpitale, sizeof(int), 1, file);
    fread(&miasteczko->straż_pożarna, sizeof(int), 1, file);
    fread(&miasteczko->szkoły, sizeof(int), 1, file);

    miasteczko->lista_możliwych_imion = malloc(4 * sizeof(char**));
    if (miasteczko->lista_możliwych_imion == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < 4; i++) {
        miasteczko->lista_możliwych_imion[i] = malloc(40 * sizeof(char*));
        if (miasteczko->lista_możliwych_imion[i] == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }

        for (int j = 0; j < 40; j++) {
            miasteczko->lista_możliwych_imion[i][j] = malloc(MAX_IMIĘ_NAZWISKO * sizeof(char));
            if (miasteczko->lista_możliwych_imion[i][j] == NULL) {
                printf("Błąd: Nie udało się przydzielić pamięci dla węzła w wczytaj_z_pliku.\n");
                exit(EXIT_FAILURE);
            }
            fread(miasteczko->lista_możliwych_imion[i][j], sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        }
    }

    fclose(file);

}