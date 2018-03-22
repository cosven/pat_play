# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        root = ListNode(0)
        root.next = head

        ever = False
        final_head = head

        group = list()
        gcurrent = head
        ghead = head
        while gcurrent is not None:
            group.append(gcurrent)
            if len(group) == k:
                if ever is False:
                    final_head = gcurrent
                    ever = True
                root = reverse_part(group, root)
                gcurrent = root.next
                group.clear()
            else:
                gcurrent = gcurrent.next
        return final_head


def print_l(head):
    while head is not None:
        print(head.val)
        head = head.next


def reverse_part(group, p_ghead):
    # group should be larger than 1
    current = group.pop()
    next_part = current.next
    p_ghead.next = current
    while True:
        try:
            node = group.pop()
        except IndexError:
            break
        current.next = node
        current = node
    current.next = next_part
    return current


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    # l2.next = l3
    # l3.next = l4
    # l4.next = l5
    print_l(Solution().reverseKGroup(l1, 2))
