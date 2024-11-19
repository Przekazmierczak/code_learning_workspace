#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"
#include "smierc.h"
#include "budynki.h"
#include "symulacja.h"
#include "menu.h"

#if defined(_WIN32) || defined(_WIN64)
#include <windows.h>  // For Sleep() on Windows
// #include <conio.h>
#else
#include <unistd.h>   // For sleep() on Linux/macOS

#endif

void symulacja(struct Miasteczko *miasteczko) {
    int następny_budynek_w_planie = rand() % 3;  // Losowy wybór budynku, który będzie budowany

    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    int ilość_lat;
    int szybkość_symulacji;

    // Pobierz ilość lat do zasymulowania od użytkownika
    printf("Podaj ilość lat do zasymulowania: ");
    int input_ilość_lat = 0;
    while (input_ilość_lat != 1) {
        input_ilość_lat = scanf("%i", &ilość_lat);  // Odczytaj ilość lat do zasymulowania
        if (input_ilość_lat != 1) {
            printf("Podaj ilość lat do zasymulowania (w formacie liczbowym): ");
            int c;
            // Oczyść bufor wejściowy, aby uniknąć zapętlenia
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    // Pobierz szybkość symulacji od użytkownika
    printf("Podaj szybkość symulacji (w ms): ");
    int input_szybkość_symulacji = 0;
    while (input_szybkość_symulacji != 1) {
        input_szybkość_symulacji = scanf("%i", &szybkość_symulacji);  // Odczytaj szybkość symulacji
        if (input_szybkość_symulacji != 1) {
            printf("Podaj szybkość symulacji (w formacie liczbowym): ");
            int c;
            // Oczyść bufor wejściowy, aby uniknąć zapętlenia
            while ((c = getchar()) != '\n' && c != EOF);
        }
    }

    // Główna pętla symulacji
    for (int i = 0; i < ilość_lat; i++) {
        // Wyczyść ekran
        #ifdef _WIN32
            system("cls");  // Windows
        #else
            system("clear");  // Linux/macOS
        #endif
        
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

        // printf("NACIŚNIJ PRZYCISK ABY ZATRZYMAĆ SYMULACJĘ");
        // if (kbhit()) {  // Nasłuchuj wciśnięcia przycisku
        //     getchar();   // Wczytaj wciśnięty klawisz aby nie wyświetlić go w terminalu
        //     system("cls");
        //     return;
        // }

        #ifdef _WIN32
            Sleep(szybkość_symulacji);
        #else
            sleep(szybkość_symulacji / 1000);
        #endif
    }
}
    