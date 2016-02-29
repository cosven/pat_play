#! /usr/bin/env python2
# -*- coding: utf-8 -*-

ROOT_ID = '01'


def line_input():
    return [int(each) for each in raw_input().split(' ')]


def node_input():
    data = raw_input().split(' ')
    p_node_id = data[0]
    children_id = data[2:]
    Node(p_node_id, children_id)
    for child_id in children_id:
        Node(child_id, parent_id=p_node_id)


class Node(object):
    all_nodes = {}

    def __init__(self, nid, children_id=None, parent_id=None):
        self.nid = nid
        self.children_id = children_id
        self.parent_id = parent_id
        Node.all_nodes[nid] = self

    def get_level(self):
        tmp_node = self
        level = 0
        while tmp_node.parent_id is not None:
            tmp_node = Node.all_nodes[tmp_node.parent_id]
            level += 1
        return level


def main():
    total_nodes, total_non_leaf_nodes = line_input()
    for i in xrange(total_non_leaf_nodes):
        node_input()
    print Node.all_nodes


if __name__ == '__main__':
    main()
