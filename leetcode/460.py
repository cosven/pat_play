obj = object()


def linkedlist_remove(node):
    """从双向链表中移除一个元素，返回新的 head 和 tail"""

    left_node = node.left
    right_node = node.right

    head = tail = obj

    if left_node is None:  # node 是 head
        head = right_node
        if head is None:  # node 是 tail
            tail = None
        else:
            head.left = None
    else:
        # 将左边和右边连接起来
        left_node.right = right_node
        if right_node is None:
            tail = left_node
        else:
            right_node.left = left_node

    node.left = None
    node.right = None
    return head, tail


class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.block = None

    def __repr__(self):
        return '{}:{}'.format(self.key, self.value)


class Block:
    def __init__(self, count, left=None, right=None):
        self.count = count

        self.left = left
        self.right = right

        self.head = None
        self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head = node
        else:
            self.tail.right = node
            node.left = self.tail
        self.tail = node
        node.block = self

    def remove(self, node):
        head, tail = linkedlist_remove(node)
        if head is not obj:
            self.head = head
        if tail is not obj:
            self.tail = tail
        node.block = None

    @property
    def empty(self):
        empty = self.head is None
        if empty:
            assert self.tail is None
        return empty


class LFUCache:

    def __init__(self, capacity):
        self._store = {}
        self._left_block = Block(1)
        self._capacity = capacity

    @property
    def full(self):
        return len(self._store) >= self._capacity

    def get(self, key):
        if key not in self._store:
            return -1
        node = self._store[key]
        self.move_node_to_next_block(node)
        return node.value

    def put(self, key, value):
        if self._capacity == 0:
            return

        if key not in self._store:
            node = Node(key, value)
            if self.full:
                self._store.pop(self._left_block.head.key)
                self.remove_node(self._left_block.head)
            self.get_or_create_count_1_block()
            self._left_block.append(node)
            self._store[key] = node
        else:
            node = self._store[key]
            node.value = value
            self.move_node_to_next_block(node)

    def create_left_block_if_needed(self):
        if self._left_block is None:
            self._left_block = Block(1)

    def get_or_create_count_1_block(self):
        if self._left_block.count != 1:
            block = Block(1)
            block.right = self._left_block
            self._left_block.left = block
            self._left_block = block

    def remove_node(self, node):
        block = node.block
        block.remove(node)
        if block.empty:
            head, _ = linkedlist_remove(block)
            if head is not obj:
                self._left_block = head
            self.create_left_block_if_needed()

    def move_node_to_next_block(self, node):
        node_count = node.block.count
        target_block = right_block = node.block.right
        if right_block is None or right_block.count != node_count + 1:
            target_block = Block(node_count + 1)
            target_block.right = right_block
            node.block.right = target_block
            target_block.left = node.block
            if right_block is not None:
                right_block.left = target_block
        self.remove_node(node)
        target_block.append(node)


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(0, 0)
    cache.put(0, 1)
    cache.put(0, 2)
    cache.put(0, 3)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache._left_block.right.count == 4

    cache = LFUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
