#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum Menu {
    RESERVE = 1,
    CANCEL,
    PRINT,
    SORT,
    BACK,
};

struct Miejsce {
    int numer;
    int zajete;
    char nazwisko[30];
};

void createParking (struct Miejsce** parking, int wielkosc);
void reserve (struct Miejsce* parking, int wielkosc);
void cancelReservation(struct Miejsce* parking, int wielkosc);
void printParking (struct Miejsce* parking, int wielkosc);
int comp(const void* a, const void* b);
void sort (struct Miejsce* parking, int wielkosc);

int main () {
    puts("Podaj wielkosc parkingu:");
    int wielkosc;
    if (scanf("%i", &wielkosc) && wielkosc > 0) {
        struct Miejsce* parking;
        createParking(&parking, wielkosc);

        enum Menu menuOpcja;
        do {
            puts("Wybierz opcje:");
            puts("1. Rezerwuj miejsce.");
            puts("2. Anuluj rezerwacje.");
            puts("3. Wyswietl stan miejsc");
            puts("4. Posortuj zajete miejsca");
            puts("5. Koniec");
            if (scanf("%i", &menuOpcja) && menuOpcja > 0 && menuOpcja < 6) {

                switch (menuOpcja) {
                    case RESERVE: {
                        reserve(parking, wielkosc);
                        break;
                    }
                    case CANCEL: {
                        cancelReservation(parking, wielkosc);
                        break;
                    }
                    case PRINT: {
                        printParking(parking, wielkosc);
                        break;
                    }
                    case SORT: {
                        sort(parking, wielkosc);
                        break;
                    }
                    case BACK: {
                        break;
                    }
                }
            } else {
                puts("Podaj wartosc liczbowa w przedziale 1-5!");
                // Czysci buffer w przypadku wprowadzenia liter
                while (getchar() != '\n');
            }
        } while (menuOpcja != BACK);
        free(parking);
    }

    return 0;
}

void createParking (struct Miejsce** parking, int wielkosc) {
    *parking = malloc(wielkosc * sizeof(struct Miejsce));
    for (int i = 0; i < wielkosc; i++) {
        (*parking)[i].numer = i + 1;
        (*parking)[i].zajete = 0;
        (*parking)[i].nazwisko[0] = '\0';
    }
}

void reserve (struct Miejsce* parking, int wielkosc) {
    puts("Podaj miejsce jakie chcesz zarezerwowac:");
    int miejsce;
    if (scanf("%i", &miejsce) && miejsce > 0 && miejsce < wielkosc + 1) {
        // Zmniejszamy o 1 poniewaz parking jest 0 index
        miejsce--;
        if (parking[miejsce].zajete) {
            puts("Miejsce jest juz zajete");
        } else {
            puts("Podaj nazwisko:");
            scanf("%s", parking[miejsce].nazwisko);
            parking[miejsce].zajete = 1;
            puts("Miejsce zostalo zarezerwowane");
        }
    } else {
        printf("Podana wartosc nie jest liczba, albo nie miesci sie w zakresie 1-%i\n", wielkosc);
        // Czysci buffer w przypadku wprowadzenia liter
        while (getchar() != '\n');
    }
}

void cancelReservation(struct Miejsce* parking, int wielkosc) {
    puts("Podaj miejsce ktore chesz zwolnic:");
    int miejsce;
    if (scanf("%i", &miejsce) && miejsce > 0 && miejsce < wielkosc + 1) {
        // Zmniejszamy o 1 poniewaz parking jest 0 index
        miejsce--;
        if (parking[miejsce].zajete) {
            parking[miejsce].zajete = 0;
            parking[miejsce].nazwisko[0] = '\0';
            puts("Miejsce zostalo zwolnione");
        } else {
            puts("Miejsce bylo juz puste");
        }
    } else {
        printf("Podana wartosc nie jest liczba, albo nie miesci sie w zakresie 1-%i\n", wielkosc);
        while (getchar() != '\n');
    }
}

void printParking (struct Miejsce* parking, int wielkosc) {
    for (int i = 0; i < wielkosc; i++) {
        if (parking[i].zajete) {
            printf("Miejsce nr %i jest zajete przez %s\n", parking[i].numer, parking[i].nazwisko);
        } else {
            printf("Miejsce nr %i jest puste\n", parking[i].numer);
        }
    }
}

int comp(const void* a, const void* b) {
    const struct Miejsce* miejsceA = (const struct Miejsce*)a;
    const struct Miejsce* miejsceB = (const struct Miejsce*)b;
    // Pusty string zawsze powinien byc mniejszy
    if (miejsceA->nazwisko[0] == '\0') {
        return 1;
    } else if (miejsceB->nazwisko[0] == '\0') {
        return -1;
    }

    return strcmp(miejsceA->nazwisko, miejsceB->nazwisko);
}

void sort (struct Miejsce* parking, int wielkosc) {
    qsort(parking, wielkosc, sizeof(struct Miejsce), comp);
    for (int i = 0; i < wielkosc; i++) {
        parking[i].numer = i + 1;
    }
}