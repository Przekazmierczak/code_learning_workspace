#include <stdbool.h>

struct Mieszkaniec {
    char* imię;
    char* nazwisko;
    char płeć; // m - mężczyzna, k - kobieta
    int wiek;
    int pensja;
};

struct Mieszkaniec* stwórz_mieszkańca(bool noworodek);