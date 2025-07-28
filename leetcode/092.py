class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # length <= 1
        if head is None or head.next is None:
            return head

        if left == right:
            return head

        # length > 1

        # 1. find left node, and save the the ptr of it's parent
        idx = 1
        left_node_parent = None  # parent of head
        current_node = head
        while idx < left:
            left_node_parent = current_node
            current_node = current_node.next
            idx += 1

        if left_node_parent is None:
            left_node = head
        else:
            left_node = left_node_parent.next

        # 2. find right node, and do reverse
        dummy_head = ListNode(0, None)
        dummy_head.next = left_node
        p1 = left_node
        p2 = left_node.next
        while idx < right:
            tmp = p2.next

            # set p2 parent to dummy_head
            p2.next = dummy_head.next
            dummy_head.next = p2

            # handle p1 p2
            p1.next = tmp
            p2 = tmp

            idx += 1

        if left_node_parent is None:
            return dummy_head.next
        else:
            left_node_parent.next = dummy_head.next
            return head
