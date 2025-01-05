/*
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {
    if (matSize * matColSize[0] != r * c) {
        r = matSize;
        c = matColSize[0];
    }
    int** res = malloc(r * sizeof(int*));

    int curr = 0;
    int currRow;
    int currCol;

    *returnSize = r;
    *returnColumnSizes = malloc(r * sizeof(int));
    for (int i = 0; i < r; i++) {
        (*returnColumnSizes)[i] = c;
    }

    for (int i = 0; i < matSize; i++) {
        for (int j = 0; j < matColSize[0]; j++) {
            currRow = curr / c;
            currCol = curr % c;
            if (currCol == 0) {
                res[currRow] = malloc(c * sizeof(int));
            }
            res[currRow][currCol] = mat[i][j];
            curr++;
        }
    }

    return res;
}