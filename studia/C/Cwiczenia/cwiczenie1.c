/*
 0. Programowanie algorytmu o strukturze liniowej.
 0.1. Wprowadź dane x = 4.5, y = 0.75×10−4, z = 0.845×102 z klawiatury.
 0.2. Oblicz wzór w kilku etapach.
 0.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
 0.4. Wytłumacz kod za pomocą komentarzy.
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;
//     const float pi = 3.14159265359;

//     float licznik, mianownik, wyraz_wolny;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     licznik = 2 * cos(x - pi/6);
//     mianownik = 0.5 + sin(y) * sin(y);
//     wyraz_wolny = 1 + ((z * z)/(3 - (z * z)/5));

//     printf("Wynik: %0.4e", licznik/mianownik + wyraz_wolny);

//     return EXIT_SUCCESS;
// }

/*
1. Programowanie algorytmu o strukturze liniowej.
1.1. Wprowadź dane x = 4.5, y = 0.75×10−4, z = 0.845×102 z klawiatury.
1.2. Oblicz wzór w kilku etapach.
1.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
1.4. Wytłumacz kod za pomocą komentarzy.
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;

//     float licznik, mianownik, wyraz_wolny;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     licznik = pow((8 + pow(fabs(x - y), 2) + 1), 1/3);
//     mianownik = x*x + y*y + 2;
//     wyraz_wolny = exp(fabs(x - y)) * pow((tan(z*z) + 1), x);

//     printf("Wynik: %0.4e", licznik/mianownik - wyraz_wolny);

//     return EXIT_SUCCESS;
// }

/*
 2. Programowanie algorytmu o strukturze liniowej.
 2.1. Wprowadź dane x = 3.74×10−2, y = −0.825, z = 0.16×102 z klawiatury.
 2.2. Oblicz wzór w kilku etapach.
 2.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
 2.4. Wytłumacz kod za pomocą komentarzy.
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;

//     float licznik, mianownik, wyraz_wolny;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     licznik = (1 + pow(sin(x + y), 2)) * pow(x, fabs(y));
//     mianownik = x - (2 * y)/(1 + x*x * y*y);
//     wyraz_wolny = pow(cos(atan(1/z)), 2);

//     printf("Wynik: %0.4e", licznik/mianownik + wyraz_wolny);

//     return EXIT_SUCCESS;
// }

/*
3. Programowanie algorytmu o strukturze liniowej.
3.1. Wprowadź dane x = 0.4 × 104, y = −0.875, z = −0.475 × 10−3 z klawiatury.
3.2. Oblicz wzór w kilku etapach.
3.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
3.4.Wytłumacz kod za pomocą komentarzy.
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;

//     float wyraz_1, wyraz_2;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     wyraz_1 = pow(fabs(cos(x) - cos(y)), 1 + pow(sin(y), 2));
//     wyraz_2 = 1 + z + pow(z, 2)/2 + pow(z, 3)/3 + pow(z, 4)/4;

//     printf("Wynik: %0.4e", wyraz_1 * wyraz_2);

//     return EXIT_SUCCESS;
// }

/*
4. Programowanie algorytmu o strukturze liniowej.
4.1. Wprowadź dane x = −15.246, y = 4.642 × 10−2, z = 20.001 × 102 z klawiatury.
4.2. Oblicz wzór w kilku etapach.
4.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
4.4. Wytłumacz kod za pomocą komentarzy.
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;

//     float wyraz_1, wyraz_2;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     wyraz_1 = log(pow(y, -sqrt(fabs(x)))) * (x - y/2);
//     wyraz_2 = pow(sin(atan(z)), 2);

//     printf("Wynik: %0.4e", wyraz_1 + wyraz_2);

//     return EXIT_SUCCESS;
// }

/*
5. Programowanie algorytmu o strukturze liniowej.
5.1. Wprowadź dane x = 16.55×10−3, y = −2.75, z = 0.15 z klawiatury.
5.2. Oblicz wzór w kilku etapach.
5.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
5.4. Wytłumacz kod za pomocą komentarzy .
*/

// #include <stdio.h>
// #include <stdlib.h>
// #include <math.h>

// int main() {
//     float x, y, z;

//     float wyraz_1, wyraz_2;

//     printf("Podaj wartosc x: ");
//     scanf_s("%f", &x);
//     printf("Podaj wartosc y: ");
//     scanf_s("%f", &y);
//     printf("Podaj wartosc z: ");
//     scanf_s("%f", &z);

//     wyraz_1 = sqrt(10 * (pow(x, 1/3) + pow(x, y + 2)));
//     wyraz_2 = pow(asin(z), 2) - fabs(x - y);

//     printf("Wynik: %0.4e", wyraz_1 * wyraz_2);

//     return EXIT_SUCCESS;
// }

/*
6. Programowanie algorytmu o strukturze liniowej.
6.1. Wprowadź dane x = 0.1722, y = 6.33, z = 3.25×10−4 z klawiatury.
6.2.Oblicz wzór w kilku etapach.
6.3. Wyświetl wynik w formacie wykładniczym z dokładnością 4 cyfr po przecinku.
6.4. Wytłumacz kod za pomocą komentarzy.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    float x, y, z;

    float wyraz_1, wyraz_2, wyraz_3;

    printf("Podaj wartosc x: ");
    scanf_s("%f", &x);
    printf("Podaj wartosc y: ");
    scanf_s("%f", &y);
    printf("Podaj wartosc z: ");
    scanf_s("%f", &z);

    wyraz_1 = 5 * atan(x);
    wyraz_2 = (1/4) * acos(x);
    wyraz_3 = (x + 3 * fabs(x - y) + x*x)/(fabs(x-y) * z + x*x);

    printf("Wynik: %0.4e", wyraz_1 - wyraz_2 * wyraz_3);

    return EXIT_SUCCESS;
}