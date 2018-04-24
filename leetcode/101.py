# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_equal(lnode, rnode):
    if lnode is not None and rnode is not None:
        return all([
            lnode.val == rnode.val,
            is_equal(lnode.left, rnode.right),
            is_equal(lnode.right, rnode.left)
        ])
    elif lnode is None and rnode is None:
        return True
    else:
        return False


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return is_equal(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(1)

    print(Solution().isSymmetric(root))
