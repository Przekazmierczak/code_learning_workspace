void śmierć_mieszkańców(struct Miasteczko *miasteczko, struct Cmentarz *cmentarz, bool pożar, bool powódź, bool trzęsienie_ziemi);
static int szansa_na_śmierć_naturalną(int wiek);
static int szansa_na_śmierć_w_przypadku_powodzi(struct Miasteczko *miasteczko);
static int szansa_na_śmierć_w_przypadku_pożaru(struct Miasteczko *miasteczko);
static int szansa_na_śmierć_w_przypadku_trzęsienia_ziemi(struct Miasteczko *miasteczko);