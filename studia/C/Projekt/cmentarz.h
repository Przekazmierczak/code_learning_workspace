#ifndef CMENTARZ_H
#define CMENTARZ_H

struct Cmentarz {
    int ilość_pozycji;
    int ilość_rzędów;
    struct Grób ***aleja;
};

struct Grób {
    struct Mieszkaniec *zmarły;
    int rok_likwidacji;
};

#endif

struct Cmentarz* stwórz_cmentarz(int ilość_pozycji);
void powiększ_cmentarz(struct Cmentarz *cmentarz);
void dodaj_zmarłego(struct Cmentarz *cmentarz, struct Mieszkaniec *mieszkaniec, int rząd_startowy);
void lista_osób_na_cmenatrzu(struct Cmentarz *cmentarz);