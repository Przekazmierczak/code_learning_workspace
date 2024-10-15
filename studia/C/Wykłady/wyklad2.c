/**************************************************
*        Listing 1: Formaty funkcji scanf         *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     int x;
//     double y;
//     printf("Podaj liczbe calkowita: ");
//     scanf_s("%d", &x);
//     printf("Podaj liczbe rzeczywista: ");
//     scanf_s("%lf", &y);
//     printf("%d %.2f\n", x, y);

//     return EXIT_SUCCESS;
// }

/**************************************************
*        Listing 2: Tekst a funkcja scanf         *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     int dzien, rok;
//     char miesiac[20];
//     printf("Podaj date: Dzien Miesiac Rok\n");
//     scanf("%d %s %d", &dzien, miesiac, &rok);
//     printf("Dzien: %d\n", dzien);
//     printf("Miesiac: %s\n", miesiac);
//     printf("Rok: %d\n", rok);

//     return EXIT_SUCCESS;
// }

/**************************************************
*      Listing 3: Inne typy a funkcja scanf       *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     int ld;
//     printf ("Podaj liczbe dziesietna : ");
//     scanf_s("%d", &ld);
//     printf("Podales liczbe : %d\n" , ld);
//     printf("Podaj liczbe osemkowa: ");
//     scanf_s("%o" , &ld );
//     printf("Osemkowo %o to dziesietnie %d\n", ld , ld);
//     printf("Podaj liczbe szesnatkowa : ");
//     scanf_s("%x" , &ld );
//     printf ("Hex: %x , Oct: %o, Dec: %d\n", ld, ld, ld);
//     return EXIT_SUCCESS;
// }

/**************************************************
*      Listing 4: IF z pojedyńczą instrukcją      *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     int a;
//     printf("Podaj wartosc zmiennej a=");
//     scanf_s("%d",&a);
//     if (a > 0) printf("Wartosc 'a' jest wieksza od zera\n");
//     if (a < 0) printf("Wartosc 'a' jest mniejsza od zera\n");
//     if (a == 0) printf("Wartosc 'a' jest rowna zero\n");
//     return EXIT_SUCCESS;
// }

/**************************************************
*       Listing 5: Czy liczba jest parzysta       *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     int liczba, reszta;
//     printf("Podaj liczbe: ");
//     scanf_s("%i", &liczba);
//     reszta = liczba % 2;
//     if (reszta == 0) printf("Liczba jest parzysta.\n");
//     else printf("Liczba jest nieparzysta.\n");
//     return EXIT_SUCCESS;
// }

/**************************************************
*      Listing 6: Czy dany rok jest przestępny     *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     int year, rem_4, rem_100, rem_400;
//     printf("Podaj rok: ");
//     scanf_s("%i", &year);
//     rem_4 = year % 4;
//     rem_100 = year % 100;
//     rem_400 = year % 400;
//     if ((rem_4 == 0 && rem_100 != 0) || rem_400 == 0)
//         printf ("Rok jest przestepny.\n");
//     else
//         printf ("Rok nie jest przestepny.\n");
//     return EXIT_SUCCESS;
// }

/**************************************************
*            Listing 8: Funkcja signum            *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     int number, sign;
//     printf("Prosze podac liczbe całkowita: ");
//     scanf_s("%i", &number);
//     if (number < 0)
//         sign = -1;
//     else
//         if (number == 0)
//             sign = 0;
//         else
//             sign = 1;
//     printf("Signum = %i\n", sign);
//     return EXIT_SUCCESS;
// }

/**************************************************
*  Listing 9, 10: Interpretator prostych wyrazen  *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     float value1, value2, value;
//     char operator;
//     puts("Podaj operator :");
//     scanf("%f %c %f", &value1, &operator, &value2);
//     if (operator == '+') {
//         value = value1 + value2;
//         printf("%.2f\n", value);
//     }
//     else
//         if (operator == '-') {
//             value = value1 - value2;
//             printf("%.2f\n", value);
//         }
//         else
//             if (operator == '*')
//                 printf("%.2f\n", value1 * value2);
//             else
//                 if (operator == '/')
//                     if (value2 == 0)
//                         printf("Dzielenie przez zero.\n");
//                     else
//                         printf("%.2f\n", value1 / value2);
//                 else
//                     printf ("Nieznany operator.\n");
//     return EXIT_SUCCESS;
// }

/**************************************************
*   Listing 15: Interpretator prostych wyrazen    *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     float value1, value2, value;
//     char operator;
//     printf ("Podaj operator.\n");
//     scanf ("%f %c %f", &value1, &operator, &value2);
//     switch (operator)
//     {
//     case '+':
//         printf("%.2f\n", value1 + value2);
//         break;
//     case '-':
//         printf("%.2f\n", value1 - value2);
//         break;
//     case '*':
//         printf("%.2f\n", value1 * value2);
//         break;
//     case '/':
//         if (value2 == 0)
//             printf("Dzielenie przez zero.\n");
//         else
//             printf("%.2f\n", value1 / value2);
//             break;
//         default:
//             printf("Nieznany operator.\n");
//             break;
//     }
//     return EXIT_SUCCESS;
// }
