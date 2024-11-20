#include <stdio.h>
#include <stdlib.h>
#include "mieszkaniec.h"
#include "miasteczko.h"

// Wybuduj nowy budynek w zależności od rodzaju planowanego budynku w przypadku posiadania wystarczającego budżetu
// W przypadku wybudowania nowego budynku zmień rodzaj planowanego budynku na kolejny losowy
int wybuduj_budynek(struct Miasteczko *miasteczko, int następny_budynek_w_planie) {
    while (
        (następny_budynek_w_planie == 0 && miasteczko->budżet > 40000000) ||  // Budżet na szpital
        (następny_budynek_w_planie == 1 && miasteczko->budżet > 25000000) ||  // Budżet na straż pożarną
        (następny_budynek_w_planie == 2 && miasteczko->budżet > 20000000)     // Budżet na szkołę
    ) {
        if (następny_budynek_w_planie == 0) {
            miasteczko->szpitale += 1;
            miasteczko->budżet -= 8000000;
        } else if (następny_budynek_w_planie == 1) {
            miasteczko->straż_pożarna += 1;
            miasteczko->budżet -= 5000000;
        } else if (następny_budynek_w_planie == 2) {
            miasteczko->szkoły += 1;
            miasteczko->budżet -= 4000000;
        }
        następny_budynek_w_planie = rand() % 3;  // Wybierz kolejny budynek losowo
    }
    return następny_budynek_w_planie;  // W przypadku braku budżetu zwróc ten sam budynek
}

// Odejmij koszty utrzymania wszystkich typów budynków od budżetu miasteczka
void utrzymanie_budynków(struct Miasteczko *miasteczko) {
    miasteczko->budżet -= miasteczko->szpitale * 200000;
    miasteczko->budżet -= miasteczko->straż_pożarna * 100000;
    miasteczko->budżet -= miasteczko->szkoły * 50000;
}

// Określ efektywność straży pożarnej w zależności od liczby mieszkańców przypadających na budynek straży
float straż_pożarna(int ilość_mieszkańców_na_sp) {
    if (ilość_mieszkańców_na_sp < 100) return 0.2;
    if (ilość_mieszkańców_na_sp < 200) return 0.4;
    if (ilość_mieszkańców_na_sp < 500) return 0.6;
    if (ilość_mieszkańców_na_sp < 1000) return 0.8;
    return 1;
}

// Określa efektywność szpitala w zależności od liczby mieszkańców przypadających na budynek szpitalny
float szpital(int ilość_mieszkańców_na_szpital) {
    if (ilość_mieszkańców_na_szpital < 100) return 1.5;
    if (ilość_mieszkańców_na_szpital < 200) return 1.4;
    if (ilość_mieszkańców_na_szpital < 500) return 1.3;
    if (ilość_mieszkańców_na_szpital < 1000) return 1.2;
    return 1;
}

// Określa efektywność szkoły w zależności od liczby mieszkańców przypadających na budynek szkolny
float szkoła(int ilość_mieszkańców_na_szkołę) {
    if (ilość_mieszkańców_na_szkołę < 100) return 1.5;
    if (ilość_mieszkańców_na_szkołę < 200) return 1.4;
    if (ilość_mieszkańców_na_szkołę < 500) return 1.3;
    if (ilość_mieszkańców_na_szkołę < 1000) return 1.2;
    return 1;
}