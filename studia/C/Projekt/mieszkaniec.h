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

char*** wczytaj_listę_imion_z_pliku();
struct Mieszkaniec* stwórz_mieszkańca(bool noworodek, char*** lista_możliwych_imion);
void praca(struct Mieszkaniec* mieszkaniec);
void uwolnij_mieszkańca(struct Mieszkaniec* mieszkaniec);