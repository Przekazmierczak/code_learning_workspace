#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include <windows.h>
#include <conio.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "smierc.h"
#include "budynki.h"
#include "symulacja.h"
#include "menu.h"

void symulacja(struct Miasteczko *miasteczko) {
    int następny_budynek_w_planie = rand() % 3;  // Losowy wybór budynku, który będzie budowany
    // Główna pętla symulacji
    for (;;) {
        system("cls");  // Wyczyść ekran (dla systemu Windows)
        
        printf("----------------------------Rok:%i-----------------------------------\n",miasteczko->rok);
        printf("Budżet: %lli\n", miasteczko->budżet);

        zarządzaj_mieszkańcami(miasteczko);  // Zwiększ wiek, przydziel pracę, wyślij na emeryturę oraz zbierz podatki od wszystkich mieszkańców
        utrzymanie_budynków(miasteczko);  // Opłać utrzymanie istniejących budynków
        następny_budynek_w_planie = wybuduj_budynek(miasteczko, następny_budynek_w_planie); // Buduj nowe budynków - o ile są fundusze

        // Losowe wystąpienie katastrof
        bool pożar = (rand() % 25 == 0);
        bool powódź = (rand() % 25 == 0);
        bool trzęsienie_ziemi = (rand() % 25 == 0);

        // Sprawdź, czy któryś z mieszkańców umarł, jeżeli tak, usuń go z listy mieszkańców i dodaj na cmentarz
        śmierć_mieszkańców(miasteczko, miasteczko->cmentarz, pożar, powódź, trzęsienie_ziemi);

        // Dodaj nowych mieszkańców do miasteczka, liczba zależy od aktualnej populacji i liczby szpitali
        for (int i = 0; i < (int)(((miasteczko->ilość_mieszkańców) / 50) * szpital(miasteczko->ilość_mieszkańców / miasteczko->szpitale)) + 1; i++) {
            dodaj_mieszkańca(miasteczko, true);
        }

        // Wyświetl informację o mieszkańcach
        printf("----------------------------Mieszkańcy---------------------------------\n");
        printf("Ilość mieszkańców: %i\n", miasteczko->ilość_mieszkańców);

        // Wyświetl informację o cmentarzu
        printf("----------------------------Cmentarz-----------------------------------\n");
        printf("Ilość rzędów: %i, ilość pozycji: %i\n", miasteczko->cmentarz->ilość_rzędów, miasteczko->cmentarz->ilość_pozycji);

        // Wyświetl informację o budynkach
        printf("----------------------------Budynki------------------------------------\n");
        printf("Ilość szpitali: %i\n", miasteczko->szpitale);
        printf("Ilość budynków straży pożarnej: %i\n", miasteczko->straż_pożarna);
        printf("Ilość budynków szkolnych: %i\n", miasteczko->szkoły);
        // printf("Stosunek %i", miasteczko->ilość_mieszkańców / miasteczko->szpitale);
        // printf("Następny budynek %i", następny_budynek_w_planie);

        // Wyświetl informację o katastrofach
        printf("----------------------------Katastrofy---------------------------------\n");
        if (!pożar && !powódź && !trzęsienie_ziemi) printf("Brak\n");
        if (pożar) printf(
            "                    (                                                \n"
            "                    )\\ )                                             \n"
            "                   (()/(             )  (                            \n"
            "                    /(_)) (   (   ( /(  )(                           \n"
            "                   (_))   )\\  )\\  )(_))(()\\                          \n"
            "                   | _ \\ ((_)((_)((_)_  ((_)                         \n"
            "                   |  _// _ \\|_ // _` || '_|                         \n"
            "                   |_|  \\___//__|\\__,_||_|                           \n"
            );
        if (powódź) printf(
            "                    O                                                \n"
            "                     o O                 O                           \n"
            "                    O o     O  O      o   o                          \n"
            "                    O  O  O   o  O   O    O   O                      \n"
            "                   O___  O   o  O   O    O _O o                      \n"
            "                   | _ \\___O_ __ _O___o __| |___                     \n"
            "                   |  _/ _ \\ V  V / _ \\/ _` |_ /                     \n"
            "                   |_| \\___/\\_/\\_/\\___/\\__,_/__|                     \n"
            );
        if (trzęsienie_ziemi) printf(
            "                                                                     \n"
            "___\\/____\\/______\\/_______\\/____________\\/_____\\/_\\/_\\/_\\/_________\\/\n"
            "                                                                     \n"
            " _____                  _            _            _                _ \n"
            "|_   _| __ _______  ___(_) ___ _ __ (_) ___   ___(_) ___ _ __ ___ (_)\n"
            "  | || '__|_  / _ \\/ __| |/ _ \\ '_ \\| |/ _ \\ |_  / |/ _ \\ '_ ` _ \\| |\n"
            "  | || |   / /  __/\\__ \\ |  __/ | | | |  __/  / /| |  __/ | | | | | |\n"
            "  |_||_|  /___\\___||___/_|\\___|_| |_|_|\\___| /___|_|\\___|_| |_| |_|_|\n"
            );
        printf("NACIŚNIJ PRZYCISK ABY ZATRZYMAĆ SYMULACJĘ");
        if (_kbhit()) {  // Nasłuchuj wciśnięcia przycisku
            _getch();   // Wszytaj wciśnięty klawisz aby nie wyświetlić go w terminalu
            system("cls");
            menu(miasteczko);
        }
        Sleep(300);
    }
}
    