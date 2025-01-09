/*
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <math.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool findTarget(struct TreeNode* root, int k) {
    struct TreeNode** arrLeft = malloc(10000 * sizeof(struct TreeNode*));
    struct TreeNode** arrRight = malloc(10000 * sizeof(struct TreeNode*));
    int* visitLeft = malloc(10000 * sizeof(int));
    int* visitRight = malloc(10000 * sizeof(int));
    struct TreeNode* curr;
    
    int leftEnd = 0;
    int rightEnd = 0;
    
    arrLeft[0] = root;
    arrRight[0] = root;
    
    visitLeft[0] = 0;
    visitRight[0] = 0;
    
    while (1) {
        while (!visitLeft[leftEnd]) {
            curr = arrLeft[leftEnd];
            if (curr->right) {
                arrLeft[leftEnd] = curr->right;
                visitLeft[leftEnd++] = 0;
            }
            arrLeft[leftEnd] = curr;
            visitLeft[leftEnd++] = 1;
            if (curr->left) {
                arrLeft[leftEnd] = curr->left;
                visitLeft[leftEnd++] = 0;
            }
            leftEnd--;
        }
        
        while (!visitRight[rightEnd]) {
            curr = arrRight[rightEnd];
            if (arrRight[rightEnd]->left) {
                arrRight[rightEnd] = curr->left;
                visitRight[rightEnd++] = 0;
            }
            arrRight[rightEnd] = curr;
            visitRight[rightEnd++] = 1;
            if (curr->right) {
                arrRight[rightEnd] = curr->right;
                visitRight[rightEnd++] = 0;
            }
            rightEnd--;
        }
        
        if (arrLeft[leftEnd] == arrRight[rightEnd]) {
            return false;
        }
        
        if (arrLeft[leftEnd]->val + arrRight[rightEnd]->val > k) {
            rightEnd--;
        } else if (arrLeft[leftEnd]->val + arrRight[rightEnd]->val < k) {
            leftEnd--;
        } else {
            return true;
        }
    }
    
    return true;
}