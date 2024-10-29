#include <stdio.h>
#include <stdlib.h>

#include "mieszkaniec.h"
#include "miasteczko.h"

int wybuduj_budynek(struct Miasteczko *miasteczko, int następny_budynek_w_planie) {
    if (następny_budynek_w_planie == 0 && miasteczko->budżet > 8000000) {
        int ilość = (int)(miasteczko->budżet / 8000000);
        miasteczko->szpitale += ilość;
        miasteczko->budżet -= ilość * 8000000;
        return rand() % 3;
    } else if (następny_budynek_w_planie == 1 && miasteczko->budżet > 5000000) {
        int ilość = (int)(miasteczko->budżet / 5000000);
        miasteczko->straż_pożarna += ilość;
        miasteczko->budżet -= ilość * 5000000;
        return rand() % 3;
    } else if (następny_budynek_w_planie == 2 && miasteczko->budżet > 4000000) {
        int ilość = (int)(miasteczko->budżet / 4000000);
        miasteczko->szkoły += ilość;
        miasteczko->budżet -= ilość * 4000000;
        return rand() % 3;
    }
    return następny_budynek_w_planie;
}

void utrzymanie_budynków(struct Miasteczko *miasteczko) {
    miasteczko->budżet -= miasteczko->szpitale * 200000;
    miasteczko->budżet -= miasteczko->straż_pożarna * 100000;
    miasteczko->budżet -= miasteczko->szkoły * 50000;
}

float straż_pożarna(int ilość_mieszkańców_na_sp) {
    if (ilość_mieszkańców_na_sp < 100) return 0.2;
    if (ilość_mieszkańców_na_sp < 200) return 0.4;
    if (ilość_mieszkańców_na_sp < 500) return 0.6;
    if (ilość_mieszkańców_na_sp < 1000) return 0.8;
    return 1;
}

float szpital(int ilość_mieszkańców_na_szpital) {
    if (ilość_mieszkańców_na_szpital < 100) return 1.5;
    if (ilość_mieszkańców_na_szpital < 200) return 1.4;
    if (ilość_mieszkańców_na_szpital < 500) return 1.3;
    if (ilość_mieszkańców_na_szpital < 1000) return 1.2;
    return 1;
}

float szkoła(int ilość_mieszkańców_na_szkołę) {
    if (ilość_mieszkańców_na_szkołę < 100) return 1.5;
    if (ilość_mieszkańców_na_szkołę < 200) return 1.4;
    if (ilość_mieszkańców_na_szkołę < 500) return 1.3;
    if (ilość_mieszkańców_na_szkołę < 1000) return 1.2;
    return 1;
}