#include "cmentarz.h"

#ifndef MIASTECZKO_H
#define MIASTECZKO_H

struct Mieszkańcy {
    struct Mieszkaniec* val;
    struct Mieszkańcy* next;
};

struct Miasteczko {
    struct Mieszkańcy* mieszkańcy;
    int budżet;
};

#endif

struct Miasteczko* stwórz_miasteczko();
void dodaj_mieszkańca(struct Miasteczko *miasteczko);
void postarzej_mieszkańców(struct Miasteczko *miasteczko);
void śmierć_naturalna(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz);
void informacje_o_mieszkańcach(struct Miasteczko *miasteczko);
void uwolnij_mieszkańców(struct Miasteczko *miasteczko);