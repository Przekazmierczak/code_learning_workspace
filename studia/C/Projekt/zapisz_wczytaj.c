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
    for (int i = 0; i < miasteczko->cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < miasteczko->cmentarz->ilość_pozycji; j++) {
            if (miasteczko->cmentarz->aleja[i][j] != NULL) {
                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->płeć), sizeof(char), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->wiek), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->pensja), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->rok_likwidacji), sizeof(int), 1, file);
            } else {
                char pusta_pozycja = '0';
                fwrite(&(pusta_pozycja), sizeof(char), 1, file);
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

}