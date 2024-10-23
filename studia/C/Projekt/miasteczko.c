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
    miasteczko->budżet = 0;
    return miasteczko;
}

void dodaj_mieszkańca(struct Miasteczko *miasteczko) {
    struct Mieszkaniec *mieszkaniec = stwórz_mieszkańca(false);
    struct Mieszkańcy *aktualny_mieszkaniec = malloc(sizeof(struct Mieszkańcy));
    if (aktualny_mieszkaniec == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla węzła w dodaj_mieszkańca.\n");
        exit(EXIT_FAILURE);
    }
    aktualny_mieszkaniec->val = mieszkaniec;
    aktualny_mieszkaniec->next = miasteczko->mieszkańcy;
    miasteczko->mieszkańcy = aktualny_mieszkaniec;
}

void postarzej_mieszkańców(struct Miasteczko *miasteczko) {
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL) {
        aktualny_mieszkaniec->val->wiek += 1;
        if (aktualny_mieszkaniec->val->wiek >= 18 && aktualny_mieszkaniec->val->pensja == 0) praca(aktualny_mieszkaniec->val);
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }
}

void śmierć_naturalna(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz) {
    if (miasteczko->mieszkańcy == NULL) {
        return;
    }

    while (miasteczko->mieszkańcy != NULL && miasteczko->mieszkańcy->val->wiek > rand() % 100) {
        dodaj_zmarłego(cmentarz, miasteczko->mieszkańcy->val, 0);
        struct Mieszkańcy *temp = miasteczko->mieszkańcy;
        miasteczko->mieszkańcy = miasteczko->mieszkańcy->next;
        free(temp);
    }

    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL && aktualny_mieszkaniec->next != NULL) {
        if (aktualny_mieszkaniec->next->val->wiek > rand() % 100) {
            dodaj_zmarłego(cmentarz, aktualny_mieszkaniec->next->val, 0);
            struct Mieszkańcy *temp = aktualny_mieszkaniec->next;
            aktualny_mieszkaniec->next = aktualny_mieszkaniec->next->next;
            free(temp);
        } else {
            aktualny_mieszkaniec = aktualny_mieszkaniec->next;
        }
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