#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "budynki.h"
#include "menu.h"

struct Miasteczko* stwórz_miasteczko(int liczba_mieszkańców, int budżet) {
    struct Miasteczko *miasteczko = malloc(sizeof(struct Miasteczko));
    if (miasteczko == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla miasteczka w stwórz_miasteczko.\n");
        exit(EXIT_FAILURE);
    }
    miasteczko->mieszkańcy = NULL;  // Inicjalizacja listy mieszkańców
    miasteczko->ilość_mieszkańców = 0; // Początkowa liczba mieszkańców
    miasteczko->rok = 0; // Rok początkowy
    miasteczko->budżet = budżet; // Budżet początkowy

    int ilość_pozycji = 10;
    miasteczko->cmentarz = stwórz_cmentarz(ilość_pozycji);

    miasteczko->szpitale = 1;  // Początkowa liczba szpitali
    miasteczko->straż_pożarna = 1;  // Początkowa liczba straży pożarnej
    miasteczko->szkoły = 1;  // Początkowa liczba szkół

    miasteczko->lista_możliwych_imion = wczytaj_listę_imion_z_pliku();

    // Dodaj początkowych mieszkańców do miasteczka
    for (int i = 0; i < liczba_mieszkańców; i++) {
        dodaj_mieszkańca(miasteczko, false);
    }

    return miasteczko;
}

void dodaj_mieszkańca(struct Miasteczko *miasteczko, bool noworodek) {
    struct Mieszkaniec *mieszkaniec = stwórz_mieszkańca(noworodek, miasteczko->lista_możliwych_imion);
    struct Mieszkańcy *aktualny_mieszkaniec = malloc(sizeof(struct Mieszkańcy));
    if (aktualny_mieszkaniec == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla węzła w dodaj_mieszkańca.\n");
        exit(EXIT_FAILURE);
    }
    aktualny_mieszkaniec->val = mieszkaniec;  // Przypisz nowego mieszkańca
    aktualny_mieszkaniec->next = miasteczko->mieszkańcy; // Dodaj nowego mieszkańca na początek listy
    miasteczko->mieszkańcy = aktualny_mieszkaniec;
    miasteczko->ilość_mieszkańców += 1; // Zwiększ liczbę mieszkańców
}

// Zwiększ wiek, przydziel pracę, wyślij na emeryturę oraz zbierz podatki od wszystkich mieszkańców
void zarządzaj_mieszkańcami(struct Miasteczko *miasteczko) {
    miasteczko->rok += 1; // Zwiększ aktualny rok
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;

    while (aktualny_mieszkaniec != NULL) {
        aktualny_mieszkaniec->val->wiek += 1; // Zwiększ wiek aktualnego mieszkańca

        // Przyznaj pracę, jeśli aktualny mieszkaniec ma 18 lat lub więcej i nie pracuje
        if (aktualny_mieszkaniec->val->wiek >= 18 && aktualny_mieszkaniec->val->pensja == 0) {
            praca(aktualny_mieszkaniec->val);
        }

        // Zakończ pracę gdy, aktualny mieszkaniec osiągnął wiek emerytalny
        if (aktualny_mieszkaniec->val->wiek >= 65 && aktualny_mieszkaniec->val->pensja != 0) {
            aktualny_mieszkaniec->val->pensja = 0;
        }
        // Zbierz podatki - wysokość podatków zwiększona jest dodatkowo od wartość stosunku ilości mieszkańców do ilości szkół
        miasteczko->budżet += (int)(aktualny_mieszkaniec->val->pensja * 0.3 * szkoła(miasteczko->ilość_mieszkańców / miasteczko->szkoły));
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }
}

void informacje_o_miasteczku(struct Miasteczko *miasteczko) {
    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif
    printf("Rok: %i\n", miasteczko->rok);
    printf("Budżet: %lli\n", miasteczko->budżet);
    printf("Ilość mieszkańców: %i\n", miasteczko->ilość_mieszkańców);
    printf("Wielkość cmentarza: %i rzędów\n", miasteczko->cmentarz->ilość_rzędów);
    printf("Ilość szpitali: %i\n", miasteczko->szpitale);
    printf("Ilość budynków straży pożarnej: %i\n", miasteczko->straż_pożarna);
    printf("Ilość budynków szkolnych: %i\n", miasteczko->szkoły);
    printf("NACIŚNIJ ENTER ABY POWRÓCIĆ DO MENU");
    while (getchar() != '\n');    // Czekaj na naciśnięcie klawisza, aby wrócić do menu
}

void informacje_o_mieszkańcach(struct Miasteczko *miasteczko) {
    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    int count = 1;
    while (aktualny_mieszkaniec != NULL) {
        // Wydrukuj dane aktualnego mieszkańca
        printf("%i: %s %s Płeć: %s Wiek: %i Pensja: %i\n",
            count,
            aktualny_mieszkaniec->val->imię,
            aktualny_mieszkaniec->val->nazwisko,
            aktualny_mieszkaniec->val->płeć == Mężczyzna ? "Mężczyna" : "Kobieta",
            aktualny_mieszkaniec->val->wiek,
            aktualny_mieszkaniec->val->pensja
            );
        aktualny_mieszkaniec = aktualny_mieszkaniec->next; // Przejdź do kolejnego mieszkańca
        count++;
    }
    printf("NACIŚNIJ ENTER ABY POWRÓCIĆ DO MENU");
    while (getchar() != '\n');    // Czekaj na naciśnięcie klawisza, aby wrócić do menu
}

void uwolnij_mieszkańców(struct Miasteczko *miasteczko) {
    while (miasteczko->mieszkańcy != NULL) {
        struct Mieszkańcy *następny_mieszkaniec = miasteczko->mieszkańcy->next;
        free(miasteczko->mieszkańcy->val->imię);
        free(miasteczko->mieszkańcy->val->nazwisko);
        free(miasteczko->mieszkańcy->val);
        free(miasteczko->mieszkańcy);
        miasteczko->mieszkańcy = następny_mieszkaniec;
    }
}