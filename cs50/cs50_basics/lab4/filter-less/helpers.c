#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gray = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue =  gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int copyRed[width];
    int copyGreen[width];
    int copyBlue[width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copyRed[j] = image[i][width - j].rgbtRed;
            copyGreen[j] = image[i][width - j].rgbtGreen;
            copyBlue[j] = image[i][width - j].rgbtBlue;
        }
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copyRed[j];
            image[i][j].rgbtGreen = copyGreen[j];
            image[i][j].rgbtBlue = copyBlue[j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int copyRed[height][width];
    int copyGreen[height][width];
    int copyBlue[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copyRed[i][j] = 0;
            copyGreen[i][j] = 0;
            copyBlue[i][j] = 0;
            int counter = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (i + k >= 0 && j + l >= 0 && i + k <= height && j + l <= width && k != 0 && l != 0)
                    {
                        copyRed[i][j] = copyRed[i][j] + image[i + k][j + l].rgbtRed;
                        copyGreen[i][j] = copyGreen[i][j] + image[i + k][j + l].rgbtGreen;
                        copyBlue[i][j] = copyBlue[i][j] + image[i + k][j + l].rgbtBlue;
                        counter++;
                    }
                }
            }
            copyRed[i][j] = round(copyRed[i][j] / counter);
            copyGreen[i][j] = round(copyGreen[i][j] / counter);
            copyBlue[i][j] = round(copyBlue[i][j] / counter);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copyRed[i][j];
            image[i][j].rgbtGreen = copyGreen[i][j];
            image[i][j].rgbtBlue = copyBlue[i][j];
        }
    }
    return;
}
