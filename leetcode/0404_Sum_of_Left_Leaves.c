/*
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
*/

#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void dfs(struct TreeNode* node, bool ifLeft, int* res) {
    if (!node->left && !node->right && ifLeft) {
        *res += node->val;
    }
    if (node->left) {  
        dfs(node->left, true, res);
    }
    if (node->right) {
        dfs(node->right, false, res);
    }
}

int sumOfLeftLeaves(struct TreeNode* root) {
    int x = 0;
    int* res = &x;
    dfs(root, false, res);
    return *res;
}