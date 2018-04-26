# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def equal(t1, t2):
    # check if t2 is a subtree of t2
    if (t1 is None) & (t2 is None):
        return True
    elif (t1 is None) ^ (t2 is None):
        return False
    return all([
        t1.val == t2.val,
        equal(t1.left, t2.left),
        equal(t1.right, t2.right),
    ])


class Solution(object):
    def isSubtree(self, t, s):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return any([
            equal(s, t),
            t and self.isSubtree(t.left, s),
            t and self.isSubtree(t.right, s),
        ])


def test_is_subtree():
    t1 = TreeNode(3)
    t1.left = TreeNode(4)
    t1.right = TreeNode(5)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(2)

    t2 = TreeNode(4)
    t2.left = TreeNode(1)
    t2.right = TreeNode(2)

    assert Solution().isSubtree(t1, t2)

    t1.left.right.left = TreeNode(0)
    assert not Solution().isSubtree(t1, t2)


def test_is_subtree_2():
    t1 = TreeNode(1)
    t1.left = TreeNode(2)

    t2 = TreeNode(1)
    assert not Solution().isSubtree(t1, t2)


if __name__ == '__main__':
    test_is_subtree_2()
    test_is_subtree()
