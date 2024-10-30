#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "budynki.h"

struct Miasteczko* stwórz_miasteczko() {
    struct Miasteczko *miasteczko = malloc(sizeof(struct Miasteczko));
    if (miasteczko == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla miasteczka w stwórz_miasteczko.\n");
        exit(EXIT_FAILURE);
    }
    miasteczko->mieszkańcy = NULL;
    miasteczko->ilość_mieszkańców = 0; // Początkowa liczba mieszkańców
    miasteczko->rok = 2024; // Rok początkowy
    miasteczko->budżet = 0; // Budżet początkowy

    int ilość_pozycji = 10;
    miasteczko->cmentarz = stwórz_cmentarz(ilość_pozycji);

    miasteczko->szpitale = 1; // Ilość szpitali
    miasteczko->straż_pożarna = 1; // Ilość budynków straży pożarnej
    miasteczko->szkoły = 1; // Ilość budynków szkolnych
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
    aktualny_mieszkaniec->next = miasteczko->mieszkańcy; // Dodaj nowego mieszkańca na początek listy
    miasteczko->mieszkańcy = aktualny_mieszkaniec;
    miasteczko->ilość_mieszkańców += 1; // Zwiększ liczbę mieszkańców
}

// Zwiększ wiek, przydziel pracę, wyślij na emeryturę oraz zbierz podatki od wszystkich mieszkańców
void zarządzaj_mieszkańcami(struct Miasteczko *miasteczko) {
    miasteczko->rok += 1; // Zwiększ aktualny rok
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;

    while (aktualny_mieszkaniec != NULL) {
        aktualny_mieszkaniec->val->wiek += 1; // Zwiększ wiek aktualnego mieszkańca

        // Przyznaj pracę, jeśli aktualny mieszkaniec ma 18 lat lub więcej i nie pracuje
        if (aktualny_mieszkaniec->val->wiek >= 18 && aktualny_mieszkaniec->val->pensja == 0) {
            praca(aktualny_mieszkaniec->val);
        }

        // Zakończ pracę gdy, aktualny mieszkaniec osiągnął wiek emerytalny
        if (aktualny_mieszkaniec->val->wiek >= 65 && aktualny_mieszkaniec->val->pensja != 0) {
            aktualny_mieszkaniec->val->pensja = 0;
        }
        // Zbierz podatki - wysokość podatków zwiększona jest dodatkowo od wartość stosunku ilości mieszkańców do ilości szkół
        miasteczko->budżet += (int)(aktualny_mieszkaniec->val->pensja * 0.3 * szkoła(miasteczko->ilość_mieszkańców / miasteczko->szkoły));
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }
}

void informacje_o_mieszkańcach(struct Miasteczko *miasteczko) {
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL) {
        // Wydrukuj dane aktualnego mieszkańca
        printf("%s %s Płeć: %c Wiek: %i Pensja: %i\n",
            aktualny_mieszkaniec->val->imię,
            aktualny_mieszkaniec->val->nazwisko,
            aktualny_mieszkaniec->val->płeć,
            aktualny_mieszkaniec->val->wiek,
            aktualny_mieszkaniec->val->pensja
            );
        aktualny_mieszkaniec = aktualny_mieszkaniec->next; // Przejdź do kolejnego mieszkańca
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