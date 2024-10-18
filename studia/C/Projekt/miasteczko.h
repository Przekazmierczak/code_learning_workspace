struct Mieszkańcy {
    struct Mieszkaniec* val;
    struct Mieszkańcy* next;
};

struct Miasteczko {
    struct Mieszkańcy* mieszkańcy;
    int budżet;
};

struct Miasteczko* stwórz_miasteczko();
void dodaj_mieszkańca(struct Miasteczko *miasteczko);
void informacje_o_mieszkańcach(struct Miasteczko *miasteczko);
void uwolnij_mieszkańców(struct Miasteczko *miasteczko);