/*
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
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
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* averageOfLevels(struct TreeNode* root, int* returnSize) {
    double* res = malloc(10000 * sizeof(double));
    *returnSize = 0;
    
    struct TreeNode* que[10000];
    int front = 0;
    int rear = 1;
    
    int level[10000];
    int prevLevel = 0;
    
    double currSum = 0;
    int currNum = 0;
    
    que[0] = root;
    level[0] = 0;
    
    while (front < rear) {
        if (level[front] != prevLevel) {
            res[(*returnSize)++] = currSum / currNum;
            currSum = 0;
            currNum = 0;
            prevLevel = level[front];
        }
        
        currSum += que[front]->val;
        currNum++;
        if (que[front]->left) {
            que[rear] = que[front]->left;
            level[rear++] = prevLevel + 1;
        }
        if (que[front]->right) {
            que[rear] = que[front]->right;
            level[rear++] = prevLevel + 1;
        }
        front++;
    }
    
    res[(*returnSize)++] = currSum / currNum;
    
    return res;
}