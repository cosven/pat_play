#! /usr/bin/env python2
# -*- coding: utf-8 -*-

'''
1. 考虑只有一个根节点的情况
'''


ROOT_ID = '01'


def line_input():
    return [int(each) for each in raw_input().split(' ')]


def node_input():
    data = raw_input().split(' ')
    p_node_id = data[0]
    children_ids = data[2:]
    if not Node.exist(p_node_id):
        Node(p_node_id, children_ids)
    else:
        Node.all_nodes[p_node_id].children_ids.extend(children_ids)
    for child_id in children_ids:
        if not Node.exist(child_id):
            Node(child_id, [], parent_id=p_node_id)


class Node(object):
    all_nodes = {}

    def __init__(self, nid, children_ids=[], parent_id=None):
        self.nid = nid
        self.children_ids = children_ids
        self.parent_id = parent_id
        Node.all_nodes[nid] = self

    def get_level(self):
        tmp_node = self
        level = 0
        while tmp_node.parent_id is not None:
            tmp_node = Node.all_nodes[tmp_node.parent_id]
            level += 1
        return level

    @classmethod
    def exist(cls, nid):
        if nid in cls.all_nodes:
            return True
        return False


def main():
    level_d = {}
    max_level = 0
    total_nodes, total_non_leaf_nodes = line_input()
    if total_non_leaf_nodes == 0:
        print 1
        return
    for i in xrange(total_non_leaf_nodes):
        node_input()

    for node in Node.all_nodes.values():
        if node.children_ids == []:
            level = node.get_level()
            if level in level_d:
                level_d[level] += 1
            else:
                level_d[level] = 1
            max_level = level if level > max_level else max_level

    for i in xrange(max_level+1):
        if i in level_d:
            if i == max_level:
                print level_d[i]
            else:
                print level_d[i],
        else:
            print 0,


if __name__ == '__main__':
    main()
