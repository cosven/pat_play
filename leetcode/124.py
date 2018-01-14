# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.visited_nodes = set()
        self.node_maxsum = {}
        self.maxsum = root.val

        # to find leaf nodes more efficiently
        self.max_degree = 1
        self.degree_nodes = defaultdict(set)
        self.calc_node_degree(root, 1)

        # O(degree)
        # while root not in self.visited_nodes:
        #     self.cur_leaf_nodes = set()
        #     self.find_cur_leaf_nodes(root)
        #     for node in self.cur_leaf_nodes:
        #         node_maxsum = self.calc_node_maxsum(node)
        #         self.node_maxsum[node] = node_maxsum
        degree = self.max_degree
        while degree >= 1:
            self.cur_leaf_nodes = set()
            for node in self.degree_nodes[degree]:
                node_maxsum = self.calc_node_maxsum(node)
                self.node_maxsum[node] = node_maxsum
            degree -= 1
        return self.maxsum

    def calc_node_degree(self, node, cur_degree):
        if node is None:
            return

        self.max_degree = max(cur_degree + 1, self.max_degree)
        self.degree_nodes[cur_degree].add(node)
        self.calc_node_degree(node.left, cur_degree + 1)
        self.calc_node_degree(node.right, cur_degree + 1)

    def calc_node_maxsum(self, node):
        """O(1)"""
        if node.left is None:
            left = 0
        else:
            left = self.node_maxsum[node.left]

        if node.right is None:
            right = 0
        else:
            right = self.node_maxsum[node.right]

        leaf_max_val = max(left, right)
        node_max = tmp_max = node.val

        # update maxsum
        if left > 0:
            tmp_max += left
        if right > 0:
            tmp_max += right
        if tmp_max > self.maxsum:
            self.maxsum = tmp_max

        # calculate node maxsum
        node_max = node.val
        if leaf_max_val > 0:
            node_max += leaf_max_val
        return node_max

    def is_leaf_node(self, node):
        """O(1)"""
        return all([node.left is None or node.left in self.visited_nodes,
                    node.right is None or node.right in self.visited_nodes])

    def find_cur_leaf_nodes(self, node):
        if any([node is None,
                node in self.visited_nodes]):
            return

        if self.is_leaf_node(node):
            self.cur_leaf_nodes.add(node)
            self.visited_nodes.add(node)
        else:
            self.find_cur_leaf_nodes(node.left)
            self.find_cur_leaf_nodes(node.right)

    def test_(self):
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node_root = TreeNode(1)
        node_root.left = node2
        node_root.right = node3

        assert self.maxPathSum(node_root) == 6


if __name__ == '__main__':
    s = Solution()
    s.test_()
