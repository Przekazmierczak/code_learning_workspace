#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"

struct Miasteczko* stwórz_miasteczko() {
    struct Miasteczko *miasteczko = malloc(sizeof(struct Miasteczko));
    if (miasteczko == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla miasteczka w stwórz_miasteczko.\n");
        exit(EXIT_FAILURE);
    }
    miasteczko->mieszkańcy = NULL;
    miasteczko->ilość_mieszkańców = 0;
    miasteczko->rok = 2024;
    miasteczko->budżet = 0;
    return miasteczko;
}

void dodaj_mieszkańca(struct Miasteczko *miasteczko, bool noworodek) {
    struct Mieszkaniec *mieszkaniec = stwórz_mieszkańca(noworodek);
    struct Mieszkańcy *aktualny_mieszkaniec = malloc(sizeof(struct Mieszkańcy));
    if (aktualny_mieszkaniec == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla węzła w dodaj_mieszkańca.\n");
        exit(EXIT_FAILURE);
    }
    aktualny_mieszkaniec->val = mieszkaniec;
    aktualny_mieszkaniec->next = miasteczko->mieszkańcy;
    miasteczko->mieszkańcy = aktualny_mieszkaniec;
    miasteczko->ilość_mieszkańców += 1;
}

void postarzej_mieszkańców(struct Miasteczko *miasteczko) {
    miasteczko->rok += 1;
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL) {
        aktualny_mieszkaniec->val->wiek += 1;
        if (aktualny_mieszkaniec->val->wiek >= 18 && aktualny_mieszkaniec->val->pensja == 0) praca(aktualny_mieszkaniec->val);
        if (aktualny_mieszkaniec->val->wiek >= 65 && aktualny_mieszkaniec->val->pensja != 0) aktualny_mieszkaniec->val->pensja = 0;
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }
}

void śmierć_naturalna(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz) {
    if (miasteczko->mieszkańcy == NULL) {
        return;
    }

    while (miasteczko->mieszkańcy != NULL && szansa_na_śmierć_naturalną(miasteczko->mieszkańcy->val->wiek) > rand() % 1000) {
        dodaj_zmarłego(cmentarz, miasteczko->mieszkańcy->val, miasteczko->rok, 0);
        struct Mieszkańcy *temp = miasteczko->mieszkańcy;
        miasteczko->mieszkańcy = miasteczko->mieszkańcy->next;
        free(temp);
        miasteczko->ilość_mieszkańców -= 1;
    }

    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL && aktualny_mieszkaniec->next != NULL) {
        if (szansa_na_śmierć_naturalną(aktualny_mieszkaniec->val->wiek) > rand() % 1000) {
            dodaj_zmarłego(cmentarz, aktualny_mieszkaniec->next->val, miasteczko->rok, 0);
            struct Mieszkańcy *temp = aktualny_mieszkaniec->next;
            aktualny_mieszkaniec->next = aktualny_mieszkaniec->next->next;
            free(temp);
            miasteczko->ilość_mieszkańców -= 1;
        } else {
            aktualny_mieszkaniec = aktualny_mieszkaniec->next;
        }
    }
}

int szansa_na_śmierć_naturalną(int wiek) {
    int przedział = wiek / 20;

    switch (przedział) {
        case 0:  // Wiek 0-19
            return 1;
        case 1:  // Wiek 20-39
            return 3;
        case 2:  // Wiek 40-59
            return 5;
        case 3:  // Wiek 60-79
            return 50;
        case 4:  // Wiek 80-99
            return 200;
        case 5:  // Wiek 100-119
            return 500;
        default: // Wiek 120 and above
            return 800;
    }
}

void informacje_o_mieszkańcach(struct Miasteczko *miasteczko) {
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL) {
        printf("%s %s Płeć: %c Wiek: %i Pensja: %i\n",
            aktualny_mieszkaniec->val->imię,
            aktualny_mieszkaniec->val->nazwisko,
            aktualny_mieszkaniec->val->płeć,
            aktualny_mieszkaniec->val->wiek,
            aktualny_mieszkaniec->val->pensja
            );
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }
}

void uwolnij_mieszkańców(struct Miasteczko *miasteczko) {
    while (miasteczko->mieszkańcy != NULL) {
        struct Mieszkańcy *następny_mieszkaniec = miasteczko->mieszkańcy->next;
        free(miasteczko->mieszkańcy->val->imię);
        free(miasteczko->mieszkańcy->val->nazwisko);
        free(miasteczko->mieszkańcy->val);
        free(miasteczko->mieszkańcy);
        miasteczko->mieszkańcy = następny_mieszkaniec;
    }
}