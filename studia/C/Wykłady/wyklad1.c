/**************************************************
*            Listing 1: Hello World               *
**************************************************/

// #include <stdio.h>

// void main() {
//     printf("Hello World!\n");
// }

/**************************************************
*  Listing 2: Hello World w środowisku Eclipse    *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main(void) {
//     puts("!!!Hello World!!!");
//     puts("!!!Hello World!!!");
//     puts("!!!Hello World!!!");
//     printf(" Hello World  !");
//     printf(" Hello World  !");
//     return EXIT_SUCCESS;
// }

/**************************************************
*             Listing 3: Przećwicz                *
**************************************************/

// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     printf("Informatyka \t Podstawy Programowania");
//     printf("\n");
//     printf(" \" C \" ");
//     return 1;
// }

/**************************************************
*Listing 4: Nazwa zmiennych i deklaracja zmiennych*
**************************************************/

// #include <stdlib.h>

// unsigned short number;
// unsigned id = 10;

// int main(void) {
//     const float podatek = 0.22;
//     int i, k = 2, z;
//     unsigned int iloscLudzi;
//     int dolna_granica = -10;
//     float cenaKawy = 5.4;
//     return EXIT_SUCCESS;
// }

/**************************************************
*       Listing 5: Stałe, komentarz liniowy       *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main(void) {
//     const float podatek = 0.22;      // komentarz linowy
//     printf("%f\n", podatek);
//     const int dwaMiliony = 2E6;
//     printf("%i\n", dwaMiliony);
//     const int liczbaHex = 0x3E8;
//     printf("%i\n", liczbaHex);
//     const double malaLiczba = 23E-10;
//     printf("%e\n", malaLiczba);
//     return EXIT_SUCCESS;
// }

/**************************************************
*          Listing 6, 7: Funkcja printf           *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main () {
//     char c = 'X';
//     int i = 425;
//     short int j = 17;
//     unsigned int u = 0xf179U;
//     long int l = 75000L;
//     long long int L = 0x1234567812345678LL;
//     float f = 12.978F;
//     double d = -97.4583;

//     printf("Integers:\n");
//     printf("%i %o %x %u\n", i, i, i, i);
//     printf("%x %X %#x %#X\n", i, i, i, i);
//     printf("%+i % i %07i %.7i\n", i, i, i, i);
//     printf("%i %o %x %u\n", j, j, j, j);
//     printf("%i %o %x %u\n", u, u, u, u);
//     printf("%ld %lo %lx %lu\n", l, l, l, l);
//     printf("%lli %llo %llx %llu\n", L, L, L, L);
//     printf("%f %e %g\n", f, f, f);
//     printf("%.2f %.2e\n", f, f);
//     printf("%.0f %.0e\n", f, f);
//     printf("%7.2f %7.2e\n", f, f);
//     printf("%f %e %g\n", d, d, d);
//     printf("%.*f\n", 3, d);
//     printf("%*.*f\n", 8, 2, d);
//     printf("%c\n", c);
//     printf("%3c%3c\n", c, c);
//     printf("%x\n", c);

//     return EXIT_SUCCESS;
// }

/**************************************************
*        Listing 8: Wyrażenia arytmetyczne        *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main (void) {
//     int a = 100, b = 2, c = 25;
//     int d;
//     d = 4;
//     int result = a - b;

//     printf ("a - b = %i\n", result);
//     result = b * c; printf ("b * c = %i\n", result);
//     result = a / c; printf ("a / c = %i\n", result);
//     result = a + b * c; printf("a + b * c = %i\n", result);
//     printf("a * b + c * d = %i\n", a * b + c * d);

//     return 0;
// }

/**************************************************
*        Listing 9: Operatory arytmetyczne        *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main (void) {
//     int a = 25 , b = 2;
//     float c = 25.0, d = 2.0;
//     printf("6 + a / 5 *b = %i\n", 6 + a / 5 * b);
//     printf("a / b * b =%i\n", a / b * b);  
//     printf("c / d * d = %f\n", c / d * d);
//     printf("-a = %i\n",-a); 
//     c= -a * b; printf("c= -a * b %f\n",c); 
//     return 0;
// }

/**************************************************
*           Listing 10: Operator modulo           *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main (void) {
//     int a = 25, b = 5, c = 10, d = 7;

//     printf("a%% b = %i\n", a % b);
//     printf("a%% c = %i\n", a % c);
//     printf("a%% d = %i\n", a % d);
//     printf("a/ d * d + a %% d = %i\n", a / d * d + a % d);
//     return 0;
// }	

/**************************************************
*     Listing 11: Konwersja i rzutowanie typów    *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main (void) {
//     float f1 = 123.125, f2; int i1, i2 = -150; char c = 'a';
//     i1 = f1;
//     printf("przypisanie %f do zmiennej int = %i\n",f1,i1);
//     f1 = i2;
//     printf("przypisanie %i do zmiennej float = %f\n",i2,f1);
//     f1 = i2 / 100;
//     printf("%i dzielone przez 100 daje %f\n",i2,f1);
//     f2 = i2 / 100.0;
//     printf("%i dzielone przez 100.0 daje %f\n",i2,f2);
//     f2 = (float)i2/100;
//     printf("(float) %i divided by 100 daje %f\n",i2,f2);
//     return 0;
// }	

/**************************************************
*           Listing 12: Zapis skrócony            *
**************************************************/

// #include <stdlib.h>
// #include <stdio.h>

// int main (void) { 
//     int a = 0, n = 0; a = n++;
//     printf("a = %d\n", a);
//     printf("n = %d\n", n);
//     a = 0; n = 0; a = ++n;
//     printf("a = %d\n", a);
//     printf("n = %d\n", n);

//     int i = 2, k = 3;
//     i += k;
//     i *= k + 2;
//     return 0;
// }