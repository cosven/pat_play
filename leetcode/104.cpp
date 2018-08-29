/*
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

------------------------------------
------------------------------------
------------------------------------

My solution: try BFS.

C programming problems:

1. how to save TreeNode object in a array?
2. how to implement a queue in C language? TODO
Maybe I should use c++ instaed ...

*/


class Solution {
public:
  int maxDepth(TreeNode* root) {
    int depth = 0;
    queue<TreeNode *> q;
    if (root == NULL)
      return 0;
    q.push(root);
    while (!q.empty()){
      depth++;
      for (int i=0, n=q.size(); i < n; i++){
        TreeNode* node;
        node = q.front();
        q.pop();
        if (node->left != NULL){
          q.push(node->left);
        }
        if (node->right != NULL){
          q.push(node->right);

        }
      }
    }
    return depth;
  }
};
