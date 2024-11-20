#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "symulacja.h"
#include "zapisz_wczytaj.h"

void menu(struct Miasteczko *miasteczko) {
    for (;;) {
        // Wyczyść ekran
        #ifdef _WIN32
            system("cls");  // Windows
        #else
            system("clear");  // Linux/macOS
        #endif
        printf("MENU\n");
        printf("Wybierz opcję:\n");
        printf("1. Kontynuuj symulacje\n");
        printf("2. Zobacz podstawowe informacje o miasteczku\n");
        printf("3. Zobacz listę mieszkańców\n");
        printf("4. Zobacz cmentarz\n");
        printf("5. Zapisz\n");
        printf("6. Wczytaj\n");
        printf("7. Zakończ program\n");

        int opcja;  // Zmienna do przechowania wybranej opcji
        int input = scanf("%i", &opcja);  // Odczytaj wejście użytkownika (opcję)

        // Jeśli podana wartość nie jest poprawna, czyści bufor wejściowy
        if (input != 1) {
            int c;
            while ((c = getchar()) != '\n' && c != EOF);  // Oczyść bufor wejścia
        } else {
            getchar();  // Usuń enter z bufforu
        }

        switch (opcja) {
            case 1:
                symulacja(miasteczko);
                break;
            case 2:
                informacje_o_miasteczku(miasteczko);
                break;
            case 3:
                informacje_o_mieszkańcach(miasteczko);
                break;
            case 4:
                lista_osób_na_cmenatrzu(miasteczko->cmentarz);
                break;
            case 5:
                zapisz_do_pliku(miasteczko);
                break;
            case 6:
                wczytaj_z_pliku(miasteczko);
                break;
            case 7:
                return;
        }
    }
}