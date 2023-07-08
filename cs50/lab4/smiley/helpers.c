#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    // RGBTRIPLE pixel = image[height][width];
    // pixel.rgbtBlue = 0x00;
    // pixel.rgbtGreen = 0x00;
    // pixel.rgbtRed = 0xff;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtBlue == 0x00 && image[i][j].rgbtGreen == 0x00 && image[i][j].rgbtRed == 0x00)
            {
                image[i][j].rgbtBlue = 0x84;
            }
        }
    }
}
