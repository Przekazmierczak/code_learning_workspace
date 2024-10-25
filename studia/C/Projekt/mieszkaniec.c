#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mieszkaniec.h"

char* imiona_męskie[40] = {
    "Antoni", "Jan", "Aleksander", "Nikodem", "Franciszek", "Jakub", "Leon", "Mikołaj", "Stanisław", "Filip",
    "Ignacy", "Szymon", "Wojciech", "Adam", "Kacper", "Tymon", "Marcel", "Maksymilian", "Michał", "Wiktor",
    "Oliwier", "Tymoteusz", "Miłosz", "Igor", "Julian", "Piotr", "Oskar", "Gabriel", "Dawid", "Krzysztof",
    "Bartosz", "Dominik", "Natan", "Bruno", "Mateusz", "Hubert", "Karol", "Alan", "Fabian", "Tomasz"
};

char* imiona_żeńskie[40] = {
    "Zofia", "Zuzanna", "Hanna", "Laura", "Maja", "Julia", "Oliwia", "Alicja", "Pola", "Lena",
    "Maria", "Emilia", "Amelia", "Antonina", "Wiktoria", "Liliana", "Iga", "Michalina", "Marcelina", "Helena",
    "Klara", "Aleksandra", "Gabriela", "Anna", "Kornelia", "Łucja", "Blanka", "Nela", "Nadia", "Natalia",
    "Jagoda", "Lilianna", "Milena", "Anastazja", "Mia", "Kaja", "Nikola", "Nina", "Weronika", "Róża"
};

char* nazwiska_męskie[40] = {
    "Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk", "Kamiński", "Lewandowski", "Zieliński", "Woźniak", "Szymański",
    "Dąbrowski", "Kozłowski", "Mazur", "Jankowski", "Kwiatkowski", "Wojciechowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski",
    "Zajac", "Pawłowski", "Król", "Michałski", "Wróbel", "Wieczorek", "Jabłoński", "Nowakowski", "Majewski", "Olszewski",
    "Dudek", "Stępień", "Jaworski", "Malinowski", "Górski", "Pawlak", "Nowicki", "Sikora", "Witkowski", "Rutkowski"
};

char* nazwiska_żeńskie[40] = {
    "Nowak", "Kowalska", "Wiśniewska", "Wójcik", "Kowalczyk", "Kamińska", "Lewandowska", "Zielińska", "Woźniak", "Szymańska",
    "Dąbrowska", "Kozłowska", "Mazur", "Jankowska", "Kwiatkowska", "Wojciechowska", "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska",
    "Pawłowska", "Zając", "Królowa", "Michałska", "Wróblewska", "Wieczorek", "Jabłońska", "Nowakowska", "Majewska", "Olszewska",
    "Dudek", "Stępień", "Jaworska", "Malinowska", "Górska", "Pawlak", "Nowicka", "Sikora", "Witkowska", "Rutkowska"
};

struct Mieszkaniec* stwórz_mieszkańca(bool noworodek) {
    struct Mieszkaniec* mieszkaniec = malloc(sizeof(struct Mieszkaniec));
    if (mieszkaniec == NULL) {
        printf("Błąd: Nie udało się przydzielić pamięci dla struktury mieszkaniecw stwórz_mieszkańca.\n");
        exit(EXIT_FAILURE);
    }

    // Losuj płeć mieszkańca
    mieszkaniec->płeć = rand() % 2 ? 'm' : 'k';

    // Przydziel imię i nazwisko w zależności od płci
    if (mieszkaniec->płeć == 'm') {
        char* imię = imiona_męskie[rand() % 40];
        mieszkaniec->imię = malloc(strlen(imię)+ 1);
        if (mieszkaniec->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->imię w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->imię, imię);
    
        char* nazwisko = nazwiska_męskie[rand() % 40];
        mieszkaniec->nazwisko = malloc(strlen(nazwisko)+ 1);
        if (mieszkaniec->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->nazwisko w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->nazwisko, nazwisko);
    } else {
        char* imię = imiona_żeńskie[rand() % 40];
        mieszkaniec->imię = malloc(strlen(imię)+ 1);
        if (mieszkaniec->imię == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->imię w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->imię, imię);

        char* nazwisko = nazwiska_żeńskie[rand() % 40];
        mieszkaniec->nazwisko = malloc(strlen(nazwisko)+ 1);
        if (mieszkaniec->nazwisko == NULL) {
            printf("Błąd: Nie udało się przydzielić pamięci dla mieszkaniec->nazwisko w stwórz_mieszkańca.\n");
            exit(EXIT_FAILURE);
        }
        strcpy(mieszkaniec->nazwisko, nazwisko);
    }

    // Ustaw wiek i pensję mieszkańca w zależności od tego, czy jest noworodkiem
    if (noworodek) {
        mieszkaniec->wiek = 0;
        mieszkaniec->pensja = 0;
    } else {
        mieszkaniec->wiek = rand() % 70;
        mieszkaniec->pensja = 0;
        // W przypadku w którym mieszkaniec ma co najmniej 18 lat, losuj czy posiada pracę
        if (mieszkaniec->wiek >= 18) {
            int i = mieszkaniec->wiek - 18;
            while (i >= 0 && mieszkaniec->pensja == 0) {
                praca(mieszkaniec);
                i--;
            }
        }
    }
    return mieszkaniec;
}

// Spróbuj przydzielić pracę mieszkańcowi, oraz ustawial losową pensję
void praca(struct Mieszkaniec* mieszkaniec) {
    if (rand() % 10 == 0) mieszkaniec->pensja = 5000 + (rand() % 10000);
}

void uwolnij_mieszkańca(struct Mieszkaniec* mieszkaniec) {
    free(mieszkaniec->imię);
    free(mieszkaniec->nazwisko);
    free(mieszkaniec);
}