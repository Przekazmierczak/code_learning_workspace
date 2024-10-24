#include <stdbool.h>

#ifndef MIESZKANIEC_H
#define MIESZKANIEC_H

struct Mieszkaniec {
    char* imię;
    char* nazwisko;
    char płeć; // m - mężczyzna, k - kobieta
    int wiek;
    int pensja;
};

#endif

struct Mieszkaniec* stwórz_mieszkańca(bool noworodek);
void praca(struct Mieszkaniec* mieszkaniec);
void uwolnij_mieszkańca(struct Mieszkaniec* mieszkaniec);