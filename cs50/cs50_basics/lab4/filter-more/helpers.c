#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int GxRed[height][width];
    int GyRed[height][width];
    int GxGreen[height][width];
    int GyGreen[height][width];
    int GxBlue[height][width];
    int GyBlue[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            GxRed[i][j] = 0;
            GyRed[i][j] = 0;
            GxGreen[i][j] = 0;
            GyGreen[i][j] = 0;
            GxBlue[i][j] = 0;
            GyBlue[i][j] = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (k == -1 && l == -1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] - image[i + k][j + l].rgbtRed;
                        GyRed[i][j] = GyRed[i][j] - image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] - image[i + k][j + l].rgbtGreen;
                        GyGreen[i][j] = GyGreen[i][j] - image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] - image[i + k][j + l].rgbtBlue;
                        GyBlue[i][j] = GyBlue[i][j] - image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == -1 && l == 0 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GyRed[i][j] = GyRed[i][j] - 2 * image[i + k][j + l].rgbtRed;
                        GyGreen[i][j] = GyGreen[i][j] - 2 * image[i + k][j + l].rgbtGreen;
                        GyBlue[i][j] = GyBlue[i][j] - 2 * image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == -1 && l == 1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] + image[i + k][j + l].rgbtRed;
                        GyRed[i][j] = GyRed[i][j] - image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] + image[i + k][j + l].rgbtGreen;
                        GyGreen[i][j] = GyGreen[i][j] - image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] + image[i + k][j + l].rgbtBlue;
                        GyBlue[i][j] = GyBlue[i][j] - image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == 0 && l == -1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] - 2 * image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] - 2 * image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] - 2 * image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == 0 && l == 1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] + 2 * image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] + 2 * image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] + 2 * image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == 1 && l == -1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] - image[i + k][j + l].rgbtRed;
                        GyRed[i][j] = GyRed[i][j] + image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] - image[i + k][j + l].rgbtGreen;
                        GyGreen[i][j] = GyGreen[i][j] + image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] - image[i + k][j + l].rgbtBlue;
                        GyBlue[i][j] = GyBlue[i][j] + image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == 1 && l == 0 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GyRed[i][j] = GyRed[i][j] + 2 * image[i + k][j + l].rgbtRed;
                        GyGreen[i][j] = GyGreen[i][j] + 2 * image[i + k][j + l].rgbtGreen;
                        GyBlue[i][j] = GyBlue[i][j] + 2 * image[i + k][j + l].rgbtBlue;
                    }
                    else if (k == 1 && l == 1 && i + k >= 0 && i + k < height && j + l >= 0 && j + l < width)
                    {
                        GxRed[i][j] = GxRed[i][j] + image[i + k][j + l].rgbtRed;
                        GyRed[i][j] = GyRed[i][j] + image[i + k][j + l].rgbtRed;
                        GxGreen[i][j] = GxGreen[i][j] + image[i + k][j + l].rgbtGreen;
                        GyGreen[i][j] = GyGreen[i][j] + image[i + k][j + l].rgbtGreen;
                        GxBlue[i][j] = GxBlue[i][j] + image[i + k][j + l].rgbtBlue;
                        GyBlue[i][j] = GyBlue[i][j] + image[i + k][j + l].rgbtBlue;
                    }
                }
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = round(sqrt(pow(GxRed[i][j], 2) + pow(GyRed[i][j], 2)));
            image[i][j].rgbtGreen = round(sqrt(pow(GxGreen[i][j], 2) + pow(GyGreen[i][j], 2)));
            image[i][j].rgbtBlue = round(sqrt(pow(GxBlue[i][j], 2) + pow(GyBlue[i][j], 2)));
            if (image[i][j].rgbtRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            if (image[i][j].rgbtGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            if (image[i][j].rgbtBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
        }
    }
    return;
}
