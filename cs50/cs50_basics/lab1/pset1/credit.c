#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long input_number = get_long("Enter your credit card: ");
    long number = input_number;
    long odd_sum = 0;
    long even_sum = 0;
    int counter = 0;

// Loop checking sum correction
    while (number != 0)
    {
        long digit = number %  10;
        number = number / 10;
        counter++;
        if (counter % 2 == 1)
        {
            odd_sum = odd_sum + digit;
        }
        else
        {
            int even_digit = digit * 2;
            if (even_digit >= 10)
            {
                even_sum = even_sum + (even_digit % 10) + (even_digit / 10);
            }
            else
            {
                even_sum = even_sum + even_digit;
            }
        }
    }
    long card_correction = odd_sum + even_sum;

    long amex_test = pow(10, (counter - 2));
    long mastercard_test = pow(10, (counter - 2));
    long visa_test = pow(10, (counter - 1));
    //American Express
    if (card_correction % 10 == 0 && counter == 15 && ((input_number / amex_test) == 37 || input_number / amex_test == 34))
    {
        printf("AMEX\n");
    }
    //MasterCard
    else if (card_correction % 10 == 0 && counter == 16 && (input_number / mastercard_test == 51 || input_number / mastercard_test == 52 || input_number / mastercard_test == 53 || input_number / mastercard_test == 54 || input_number / mastercard_test == 55))
    {
        printf("MASTERCARD\n");
    }
    //Visa
    else if (card_correction % 10 == 0 && (counter == 13 || counter == 16) && input_number / visa_test == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
