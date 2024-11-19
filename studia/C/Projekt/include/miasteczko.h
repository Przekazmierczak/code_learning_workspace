#include "cmentarz.h"

#ifndef MIASTECZKO_H
#define MIASTECZKO_H

struct Mieszkańcy {
    struct Mieszkaniec* val;
    struct Mieszkańcy* next;
};

struct Miasteczko {
    struct Mieszkańcy* mieszkańcy;
    int ilość_mieszkańców;
    int rok;
    long long budżet;
    struct Cmentarz* cmentarz;
    int szpitale;
    int straż_pożarna;
    int szkoły;
    char*** lista_możliwych_imion;
};

#endif

struct Miasteczko* stwórz_miasteczko(int liczba_mieszkańców, int budżet);
void dodaj_mieszkańca(struct Miasteczko *miasteczko, bool noworodek);
void zarządzaj_mieszkańcami(struct Miasteczko *miasteczko);
void informacje_o_miasteczku(struct Miasteczko *miasteczko);
void informacje_o_mieszkańcach(struct Miasteczko *miasteczko);
void uwolnij_mieszkańców(struct Miasteczko *miasteczko);