#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "mieszkaniec.h"
#include "miasteczko.h"
#include "cmentarz.h"

extern int ILOŚĆ_KATEGORII;
extern int ILOŚĆ_IMION_NAZWISK;
extern int MAX_IMIĘ_NAZWISKO;

// Funkcja zapisująca dane miasteczka do pliku binarnego
void zapisz_do_pliku(struct Miasteczko *miasteczko) {
    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    printf("TRWA ZAPISYWANIE...\n");

    // Otwórz plik binarny do zapisu
    FILE *file = fopen("zapis.bin", "wb");

    if (!file){
        printf("Nie udało się utworzyć pliku do zapisu");
        exit(EXIT_FAILURE);
    }

    // Zapisz podstawowe informacje o miasteczku
    fwrite(&miasteczko->ilość_mieszkańców, sizeof(int), 1, file);
    fwrite(&miasteczko->rok, sizeof(int), 1, file);
    fwrite(&miasteczko->budżet, sizeof(long long), 1, file);

    // Zapisz dane każdego mieszkańca
    struct Mieszkańcy *aktualny_mieszkaniec = miasteczko->mieszkańcy;
    for (int i = 0; i < miasteczko->ilość_mieszkańców; i++) {
        fwrite(aktualny_mieszkaniec->val->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        fwrite(aktualny_mieszkaniec->val->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        fwrite(&(aktualny_mieszkaniec->val->płeć), sizeof(char), 1, file);
        fwrite(&(aktualny_mieszkaniec->val->wiek), sizeof(int), 1, file);
        fwrite(&(aktualny_mieszkaniec->val->pensja), sizeof(int), 1, file);
        aktualny_mieszkaniec = aktualny_mieszkaniec->next;
    }

    // Zapisz dane cmentarza
    fwrite(&miasteczko->cmentarz->ilość_pozycji,sizeof(int), 1, file);
    fwrite(&miasteczko->cmentarz->ilość_rzędów, sizeof(int), 1, file);

    bool pusta_pozycja;  // Zmienna pomocnicza do sprawdzenia, czy pozycja na cmentarzu jest pusta

    for (int i = 0; i < miasteczko->cmentarz->ilość_rzędów; i++) {
        for (int j = 0; j < miasteczko->cmentarz->ilość_pozycji; j++) {
            // W przypadku w którym w grobie jest zmarły zapisz od pliku pustą_pozycję jako true a następnie dane zmarłego
            if (miasteczko->cmentarz->aleja[i][j] != NULL) {
                pusta_pozycja = false;
                fwrite(&(pusta_pozycja), sizeof(bool), 1, file);

                // Zapisz dane zmarłego w grobie
                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->płeć), sizeof(char), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->wiek), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->zmarły->pensja), sizeof(int), 1, file);
                fwrite(&(miasteczko->cmentarz->aleja[i][j]->rok_likwidacji), sizeof(int), 1, file);
            // W przypadku w którym w grób jest pusty zapisz od pliku pustą_pozycję jako false i kontynuuj
            } else {
                pusta_pozycja = true;
                fwrite(&(pusta_pozycja), sizeof(bool), 1, file);
            }
        }
    }

    // Zapisz dane dotyczące infrastruktury miejskiej
    fwrite(&miasteczko->szpitale, sizeof(int), 1, file);
    fwrite(&miasteczko->straż_pożarna, sizeof(int), 1, file);
    fwrite(&miasteczko->szkoły, sizeof(int), 1, file);

    // Zapisz listę możliwych imion
    for (int i = 0; i < ILOŚĆ_KATEGORII; i++) {
        for (int j = 0; j < ILOŚĆ_IMION_NAZWISK; j++) {
            fwrite(miasteczko->lista_możliwych_imion[i][j], sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        }
    }

    fclose(file);  // Zamknij plik

    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    printf("Zapisywanie zakończono sukcesem\n");
    printf("NACIŚNIJ ENTER ABY POWRÓCIĆ DO MENU");
    while (getchar() != '\n');    // Czekaj na naciśnięcie klawisza, aby wrócić do menu
}

// Funkcja wczytująca dane miasteczka z pliku binarnego
void wczytaj_z_pliku(struct Miasteczko *miasteczko) {
    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif

    printf("TRWA WCZYTYWANIE...\n");

    // Otwórz plik binarny do odczytu
    FILE *file = fopen("zapis.bin", "rb");

    if (!file){
        // Wyczyść ekran
        #ifdef _WIN32
            system("cls");  // Windows
        #else
            system("clear");  // Linux/macOS
        #endif
        
        printf("Wczytywanie zakończono niepowodzeniem - brak pliku\n");
        printf("NACIŚNIJ ENTER ABY POWRÓCIĆ DO MENU");
        while (getchar() != '\n');    // Czekaj na naciśnięcie klawisza, aby wrócić do menu
        return;
    }

    // Zwolnij wcześniej zarezerwowaną pamięć
    uwolnij_cmentarz(miasteczko->cmentarz);
    uwolnij_mieszkańców(miasteczko);


    // Wczytaj dane podstawowe miasteczka
    fread(&miasteczko->ilość_mieszkańców, sizeof(int), 1, file);
    fread(&miasteczko->rok, sizeof(int), 1, file);
    fread(&miasteczko->budżet, sizeof(long long), 1, file);

    miasteczko->mieszkańcy = NULL;

    struct Mieszkańcy *aktualny = NULL;
    struct Mieszkańcy **następny = &miasteczko->mieszkańcy;

     // Wczytaj dane mieszkańców
    for (int i = 0; i < miasteczko->ilość_mieszkańców; i++) {
        aktualny = malloc(sizeof(struct Mieszkańcy));
        if (aktualny == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        aktualny->val = malloc(sizeof(struct Mieszkaniec));
        if (aktualny->val == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }

        aktualny->val->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (aktualny->val->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        fread(aktualny->val->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

        aktualny->val->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
        if (aktualny->val->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        fread(aktualny->val->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

        fread(&(aktualny->val->płeć), sizeof(char), 1, file);
        fread(&(aktualny->val->wiek), sizeof(int), 1, file);
        fread(&(aktualny->val->pensja), sizeof(int), 1, file);

        *następny = aktualny;
        następny = &aktualny->next;
    }

    *następny = NULL;

    // Wczytaj dane cmentarza
    fread(&miasteczko->cmentarz->ilość_pozycji,sizeof(int), 1, file);
    fread(&miasteczko->cmentarz->ilość_rzędów, sizeof(int), 1, file);

    // Alokuj pamięć dla alei cmentarza
    miasteczko->cmentarz->aleja = malloc(miasteczko->cmentarz->ilość_rzędów * sizeof(struct Grób**));
    if (miasteczko->cmentarz->aleja == NULL) {
        printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
        exit(EXIT_FAILURE);
    }

    bool pusta_pozycja;  // Zmienna pomocnicza do sprawdzenia, czy pozycja na cmentarzu jest pusta

    // Wczytaj dane grobów
    for (int i = 0; i < miasteczko->cmentarz->ilość_rzędów; i++) {
        miasteczko->cmentarz->aleja[i] = malloc(miasteczko->cmentarz->ilość_pozycji * sizeof(struct Grób*));
        if (miasteczko->cmentarz->aleja[i] == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }
        for (int j = 0; j < miasteczko->cmentarz->ilość_pozycji; j++) {
            // Wczytaj wartość dla pusta_pozycja z pliku
            fread(&pusta_pozycja, sizeof(bool), 1, file);

            // W przypadku w którym wartość dla pusta_pozycja jest false następne bity dotyczą danych zmarłego
            if (pusta_pozycja == false) {
                // Wczytaj dane zmarłego w grobie
                miasteczko->cmentarz->aleja[i][j] = malloc(sizeof(struct Grób));
                if (miasteczko->cmentarz->aleja[i][j] == NULL) {
                    printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }

                miasteczko->cmentarz->aleja[i][j]->zmarły = malloc(sizeof(struct Mieszkaniec));
                if (miasteczko->cmentarz->aleja[i][j]->zmarły == NULL) {
                    printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }

                miasteczko->cmentarz->aleja[i][j]->zmarły->imię = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
                if (miasteczko->cmentarz->aleja[i][j]->zmarły->imię == NULL) {
                    printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }
                fread(miasteczko->cmentarz->aleja[i][j]->zmarły->imię, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

                miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko = malloc(sizeof(char) * MAX_IMIĘ_NAZWISKO);
                if (miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko == NULL) {
                    printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
                    exit(EXIT_FAILURE);
                }
                fread(miasteczko->cmentarz->aleja[i][j]->zmarły->nazwisko, sizeof(char), MAX_IMIĘ_NAZWISKO, file);

                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->płeć), sizeof(char), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->wiek), sizeof(int), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->zmarły->pensja), sizeof(int), 1, file);
                fread(&(miasteczko->cmentarz->aleja[i][j]->rok_likwidacji), sizeof(int), 1, file);
            // W przypadku w którym wartość dla pusta_pozycja jest true brak danych dotyczących zmarłego więc pętlę należy kontynuować
            } else {
                miasteczko->cmentarz->aleja[i][j] = NULL;
            }
        }
    }

    // Wczytaj dane dotyczące infrastruktury miejskiej
    fread(&miasteczko->szpitale, sizeof(int), 1, file);
    fread(&miasteczko->straż_pożarna, sizeof(int), 1, file);
    fread(&miasteczko->szkoły, sizeof(int), 1, file);

    // Wczytaj listę możliwych imion
    miasteczko->lista_możliwych_imion = malloc(ILOŚĆ_KATEGORII * sizeof(char**));
    if (miasteczko->lista_możliwych_imion == NULL) {
        printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < ILOŚĆ_KATEGORII; i++) {
        miasteczko->lista_możliwych_imion[i] = malloc(ILOŚĆ_IMION_NAZWISK * sizeof(char*));
        if (miasteczko->lista_możliwych_imion[i] == NULL) {
            printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
            exit(EXIT_FAILURE);
        }

        for (int j = 0; j < ILOŚĆ_IMION_NAZWISK; j++) {
            miasteczko->lista_możliwych_imion[i][j] = malloc(MAX_IMIĘ_NAZWISKO * sizeof(char));
            if (miasteczko->lista_możliwych_imion[i][j] == NULL) {
                printf("Błąd: Nie udało się przydzielić w wczytaj_z_pliku.\n");
                exit(EXIT_FAILURE);
            }
            fread(miasteczko->lista_możliwych_imion[i][j], sizeof(char), MAX_IMIĘ_NAZWISKO, file);
        }
    }

    fclose(file);

    // Wyczyść ekran
    #ifdef _WIN32
        system("cls");  // Windows
    #else
        system("clear");  // Linux/macOS
    #endif
    
    printf("Wczytywanie zakończono sukcesem\n");
    printf("NACIŚNIJ ENTER ABY POWRÓCIĆ DO MENU");
    while (getchar() != '\n');    // Czekaj na naciśnięcie klawisza, aby wrócić do menu
}