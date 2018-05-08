class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def serialize(self, root):
        # write your code here
        l = []
        q = list()
        if root is None:
            return []
        q.append(root)
        while q:
            node = q.pop(0)
            if node is not None:
                l.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                l.append(None)
                continue
        return l

    def deserialize(self, data):
        if not data:
            return None
        root = TreeNode(data.pop(0))
        q = [root]
        while len(data) > 1:
            node = q.pop(0)
            if node is not None:
                val = data.pop(0)
                if val is not None:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = data.pop(0)
                if val is not None:
                    node.right = TreeNode(val)
                    q.append(node.right)
        else:
            if data:
                node = q.pop(0)
                node.left = TreeNode(data[0])
        return root


class SolutionPreorder(object):
    """
    Can preorder traversal result reconstruct the binary tree?
    """
    def serialize(self, root):
        l = []
        if root is None:
            return []
        self.preorder_traversal(root, l)
        return l

    def preorder_traversal(self, node, l):
        if node is not None:
            l.append(node.val)
            self.preorder_traversal(node.left, l)
            self.preorder_traversal(node.right, l)
        else:
            l.append(None)

    def deserialize(self, l):
        if not l:
            return None
        root = TreeNode(l.pop(0))
        q = [root]  # queue, FIFO
        left_ok = False
        while l:
            if left_ok is True:
                if q:
                    node = q.pop()
                else:
                    break
            else:
                node = q[-1]
            val = l.pop(0)
            if val is None:
                left_ok = True
            elif left_ok is False:
                node.left = TreeNode(val)
                q.append(node.left)
            else:
                node.right = TreeNode(val)
                q.append(node.right)
                left_ok = False
        return root

    def deserialize_2(self, l):
        if not l:
            return None
        root = TreeNode(l.pop(0))
        root.left = self.detraversal(l)
        root.right = self.detraversal(l)
        return root

    def detraversal(self, l):
        if not l:
            return None
        val = l.pop(0)
        if val is not None:
            node = TreeNode(val)
            node.left = self.detraversal(l)
            node.right = self.detraversal(l)
            return node
        return None


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    #l = Solution().serialize(root)
    #aroot = Solution().deserialize(l)
    #al = Solution().serialize(aroot)
    l = SolutionPreorder().serialize(root)
    print(l)
    tree = SolutionPreorder().deserialize(l)
    al = SolutionPreorder().serialize(tree)
    print(al)
    tree = SolutionPreorder().deserialize_2(al)
    aal = SolutionPreorder().serialize(tree)
    print(aal)
