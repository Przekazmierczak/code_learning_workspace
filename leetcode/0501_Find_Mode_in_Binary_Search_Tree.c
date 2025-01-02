/*
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [1,null,2,2]
Output: [2]

Example 2:
Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
*/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>


//Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void dfs(struct TreeNode* node, int* prev, int* count, int* currMax, int* res, int* returnSize, bool firstIteration) {
    if (node->left) {
        dfs(node->left, prev, count, currMax, res, returnSize, firstIteration);
    }
    
    if (*prev == node->val) {
        (*count)++;
    } else {
        *prev = node->val;
        *count = 1;
    }
    if (firstIteration && *count > *currMax) {
        *currMax = *count;
    }
    if (!firstIteration && *count == *currMax) {
        res[(*returnSize)++] = node->val;
        if (*returnSize % 100 == 0) {
            res = realloc(res, (*returnSize + 100) * sizeof(int));
        }
    }
    
    if (node->right) {
        dfs(node->right, prev, count, currMax, res, returnSize, firstIteration);
    }
}

int* findMode(struct TreeNode* root, int* returnSize) {
    int* res = malloc(100 * sizeof(int));
    *returnSize = 0;
    int* prev = malloc(sizeof(int));
    *prev = 100001;
    int* count = malloc(sizeof(int));
    *count = 1;
    int* currMax = malloc(sizeof(int));
    *currMax = 0;
    
    dfs(root, prev, count, currMax, res, returnSize, true);
    *prev = 100001;
    *count = 1;
    dfs(root, prev, count, currMax, res, returnSize, false);
    
    return res;
}