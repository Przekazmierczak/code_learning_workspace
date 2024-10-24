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
    int budżet;
};

#endif

struct Miasteczko* stwórz_miasteczko();
void dodaj_mieszkańca(struct Miasteczko *miasteczko, bool noworodek);
void postarzej_mieszkańców(struct Miasteczko *miasteczko);
void śmierć_naturalna(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz);
int szansa_na_śmierć_naturalną(int wiek);
void informacje_o_mieszkańcach(struct Miasteczko *miasteczko);
void uwolnij_mieszkańców(struct Miasteczko *miasteczko);