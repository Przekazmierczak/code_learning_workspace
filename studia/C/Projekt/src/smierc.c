#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "smierc.h"
#include "budynki.h"

void śmierć_mieszkańców(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz, bool pożar, bool powódź, bool trzęsienie_ziemi) {
    if (miasteczko->mieszkańcy == NULL) return; // Powróć gdy brak jest mieszkańców

    int rząd = 0;
    int pozycja = 0;

    // Sprawdź mieszkańców na początku listy
    bool śmierć_pierwszego_mieszkańca = true;
    while (miasteczko->mieszkańcy != NULL && śmierć_pierwszego_mieszkańca) {
        int szansa_na_śmierc = szansa_na_śmierć_naturalną(miasteczko->mieszkańcy->val->wiek);
        śmierć_pierwszego_mieszkańca = false;
        if (pożar) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_pożaru(miasteczko);
        }
        if (powódź) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_powodzi(miasteczko);
        }
        if (trzęsienie_ziemi) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_trzęsienia_ziemi(miasteczko);
        }
        if (szansa_na_śmierc > rand() % 1000) {
            dodaj_zmarłego(cmentarz, miasteczko->mieszkańcy->val, miasteczko->rok, &rząd, &pozycja);
            struct Mieszkańcy *temp = miasteczko->mieszkańcy;
            miasteczko->mieszkańcy = miasteczko->mieszkańcy->next; // Usuń aktualnego mieszkańca z listy
            free(temp); // Zwolnij pamięć zarezerwowaną na aktualnego mieszkańca
            miasteczko->ilość_mieszkańców -= 1; // Zmniejsz liczbę mieszkańców
            śmierć_pierwszego_mieszkańca = true;
        }
    }

    // Sprawdź mieszkańców w pozostałej części listy
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    while (aktualny_mieszkaniec != NULL && aktualny_mieszkaniec->next != NULL) {
        int szansa_na_śmierc = szansa_na_śmierć_naturalną(miasteczko->mieszkańcy->val->wiek);
        if (pożar) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_pożaru(miasteczko);
        }
        if (powódź) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_powodzi(miasteczko);
        }
        if (trzęsienie_ziemi) {
            szansa_na_śmierc += szansa_na_śmierć_w_przypadku_trzęsienia_ziemi(miasteczko);
        }
        if (szansa_na_śmierc > rand() % 1000) {
            dodaj_zmarłego(cmentarz, aktualny_mieszkaniec->next->val, miasteczko->rok, &rząd, &pozycja); // Dodaje zmarłego na cmentarz
            struct Mieszkańcy *temp = aktualny_mieszkaniec->next;
            aktualny_mieszkaniec->next = aktualny_mieszkaniec->next->next; // Usuń aktualnego mieszkańca z listy
            free(temp); // Zwolnij pamięć zarezerwowaną na aktualnego mieszkańca
            miasteczko->ilość_mieszkańców -= 1; // Zmniejsza liczbę mieszkańców
        } else {
            aktualny_mieszkaniec = aktualny_mieszkaniec->next; // Przejdź do kolejnego mieszkańca
        }
    }
}

int szansa_na_śmierć_naturalną(int wiek) {
    int przedział = wiek / 20; // Podziel wiek na przedziały co 20 lat
    switch (przedział) {
        case 0:  // Wiek 0-19
            return 1;
        case 1:  // Wiek 20-39
            return 2;
        case 2:  // Wiek 40-59
            return 4;
        case 3:  // Wiek 60-79
            return 50;
        case 4:  // Wiek 80-99
            return 300;
        case 5:  // Wiek 100-119
            return 800;
        default: // Wiek 120 i wyżej
            return 950;
    }
}

// Określ dodatkowe ryzyko śmierci w wyniku pożaru - wartość zależy od stosunku ilości mieszkańców do straży pożarnej
int szansa_na_śmierć_w_przypadku_pożaru(struct Miasteczko *miasteczko) {
    return 150 * straż_pożarna(miasteczko->ilość_mieszkańców / miasteczko->straż_pożarna);
}

// Określ dodatkowe ryzyko śmierci w wyniku powodzi - wartość zależy od stosunku ilości mieszkańców do straży pożarnej
int szansa_na_śmierć_w_przypadku_powodzi(struct Miasteczko *miasteczko) {
    return 100 * straż_pożarna(miasteczko->ilość_mieszkańców / miasteczko->straż_pożarna);
}

// Określ dodatkowe ryzyko śmierci w wyniku trzęsienia ziemi - wartość zależy od stosunku ilości mieszkańców do straży pożarnej
int szansa_na_śmierć_w_przypadku_trzęsienia_ziemi(struct Miasteczko *miasteczko) {
    return 50 * straż_pożarna(miasteczko->ilość_mieszkańców / miasteczko->straż_pożarna);
}