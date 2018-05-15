import time


class Node:
    def __init__(self, key, value, count, ts):
        self._left = None
        self._right = None

        self.key = key
        self.value = value
        self.count = count
        self.ts = ts

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node._right = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node._left = self



class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self._cache = {}
        self.root = None
        self.latest_not_visited_node = None

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self._cache:
            node = self._cache[key]
            # 这个点感觉题目说的不是特别清楚
            node.count += 1
            node.ts = time.time()
            node.value = value
            self.update_node_pos(node)
            return

        node = Node(key, value, 0, time.time())
        if len(self._cache.keys()) == self.capacity:
            self._cache.pop(self.root.key)

            if self.latest_not_visited_node is None:
                self.root = self.root.right
                node.right = self.root
                self.root = node
            elif self.latest_not_visited_node.key == self.root.key:
                node.right = self.root.right
                self.root = node
            else:
                self.root = self.root.right
                node.right = self.latest_not_visited_node.right
                self.latest_not_visited_node.right = node
        else:
            if self.root is None:
                self.root = node
            else:
                if self.latest_not_visited_node is not None:
                    node.right = self.latest_not_visited_node.right
                    self.latest_not_visited_node.right = node
                else:
                    node.right = self.root
                    self.root = node
        self.latest_not_visited_node = node
        self._cache[key] = node
        self.root.left = None

    def get(self, key):
        # write your code here
        if key in self._cache:
            node = self._cache[key]
            node.count += 1
            node.ts = time.time()

            self.update_node_pos(node)
            return node.value
        return -1

    def update_node_pos(self, node):
        if self.latest_not_visited_node is not None:
            if node.key == self.latest_not_visited_node.key:
                self.latest_not_visited_node = node.left

        right_node = node.right
        if right_node is None or right_node.count > node.count + 1:
            return
        if node.left is None:
            assert node.key == self.root.key
            node.right = right_node.right
            self.root = right_node
            self.root.right = node
            self.root.left = None
            return

        node.left.right = right_node
        node.right = right_node.right
        right_node.right = node


if __name__ == '__main__':
    cache = LFUCache(3)
    cache.put(2,2)
    cache.put(1,1)
    cache.get(2)
    cache.get(1)
    cache.put(3, 3)
    cache.put(4, 4)
    assert cache.get(3) == -1


    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.get(3)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

    cache = LFUCache(3)
    cache.put(2, 2)
    cache.put(1, 1)
    cache.get(2)
    print(cache._cache[1].left is None)
    cache.get(1)
    print(cache.latest_not_visited_node is None)
    cache.get(2)
    print(cache._cache[1].left is None)
    cache.put(3, 3)
    print(cache._cache[1].left is not None)
    cache.put(4, 4)
    print(cache.latest_not_visited_node.key == 4)
    print(cache.root.key == 4)
    cache.get(3)
    print(cache.root.key == 4)
    cache.get(2)
    cache.get(1)
    print(cache.root.key == 4)
    cache.get(4)
