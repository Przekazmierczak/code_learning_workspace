/*
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]

Output: 1
Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 10^5
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

void dfs(struct TreeNode* node, int* prev, int* res) {
    if (node->left) {
        dfs(node->left, prev, res);
    }

    if (*prev != -1 && abs(*prev - node->val) < *res) {
        *res = abs(*prev - node->val);
    }
    *prev = node->val;

    if (node->right) {
        dfs(node->right, prev, res);
    }

}

int getMinimumDifference(struct TreeNode* root) {
    int* prev = malloc(sizeof(int));
    *prev = -1;
    int* res = malloc(sizeof(int));
    *res = pow(10, 5);

    dfs(root, prev, res);

    return *res;
}