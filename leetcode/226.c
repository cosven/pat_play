#include <stdio.h>


int main()
{

}

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


struct TreeNode* invertTree(struct TreeNode* root) {
    struct TreeNode *left;

    /* NOTE: 好奇这里到底要不要分配内存给 left，结论似乎是不需要 */

    if (!root)
        return root;

    left = root->left;
    root->left = root->right;
    root->right = left;

    if (root->left)
        invertTree(root->left);
    if (root->right)
        invertTree(root->right);

    return root;
}
