/*
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
Note: The merging process must start from the root nodes of both trees.

---------------------------------------------
---------------------------------------------
---------------------------------------------

a simple tree traversal problem, use a recursive method.
*/


#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2) {
    struct TreeNode *node;
    struct TreeNode *t;

    /*
       NOTE: when to free this memory?
       A: maybe we can implement a function to free those memory
       allocated for a whole tree.
     */
    node = (struct TreeNode *) malloc(sizeof(struct TreeNode));

    if (t1 != NULL && t2 != NULL)
    {
        node->val = t1->val + t2->val;
        node->left = mergeTrees(t1->left, t2->left);
        node->right = mergeTrees(t1->right, t2->right);
        return node;
    }
    else if ((t1 != NULL && t2 == NULL) || (t1 == NULL && t2 != NULL))
    {
        if (t1 == NULL)
            t = t2;
        else
            t = t1;

        node->val = t->val;
        node->left = mergeTrees(t->left, NULL);
        node->right = mergeTrees(t->right, NULL);
        return node;
    }
    return NULL;
}
