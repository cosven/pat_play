class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return self.val


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._total = 0
        self._head = None
        self._tail = None
        self._store = {}  # {node, value}
        self._key_node = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._key_node:
            return -1
        else:
            node = self._key_node[key]
            self.update_pos(node)
            return self._store[node]

    def update_pos(self, node):
        if self._tail == node:
            return

        if node == self._head:
            self._head = node.next
            self._head.prev = None

            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = self._tail
            self._tail.next = node
            self._tail = node

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self._capacity <= 0:
            return

        if key not in self._key_node:
            if self._total >= self._capacity:
                self._store.pop(self._head)
                self._key_node.pop(self._head.val)
                self._total -= 1

                if self._total == 0:
                    self._head = self._tail = None
                else:
                    self._head = self._head.next
                    self._head.prev = None

            node = Node(key)
            self._key_node[key] = node
            self._store[node] = value

            if self._total == 0:
                self._head = self._tail = node
            else:
                node.prev = self._tail
                self._tail.next = node
                self._tail = node

            self._total += 1
        else:
            node = self._key_node[key]
            self._store[node] = value
            self.update_pos(node)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache = LRUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1

    cache = LRUCache(1)
    cache.put(2, 1)
    assert cache.get(2) == 1
    cache.put(3, 2)
    assert cache.get(2) == -1
    assert cache.get(3) == 2
