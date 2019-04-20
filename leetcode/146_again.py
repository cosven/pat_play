class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity):
        self._store = {}
        self._capacity = capacity
        self._root = None

    @property
    def full(self):
        return len(self._store) == self._capacity

    @property
    def empty(self):
        return not bool(self._store)

    def get(self, key):
        if key not in self._store:
            return -1
        node = self._store[key]
        self._upgrade_node(node)
        return node.value

    def _del_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _upgrade_node(self, node):
        if node is not self._root:
            self._del_node(node)
            self._set_root(node)

    def _set_root(self, node):
        node.next = self._root
        node.prev = self._root.prev
        self._root.prev.next = node
        self._root.prev = node
        self._root = node

    def put(self, key, value):
        if self._capacity <= 0:
            return

        if key in self._store:
            node = self._store[key]
            node.value = value
            self._upgrade_node(node)
        else:
            node = Node(key=key, value=value)
            if self.full:
                root_prev = self._root.prev
                self._store.pop(root_prev.key)
                if root_prev is self._root:
                    self._root = None
                else:
                    self._del_node(self._root.prev)
            if self.empty:
                node.prev = node.next = self._root = node
            else:
                self._set_root(node)
            self._store[key] = node


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
