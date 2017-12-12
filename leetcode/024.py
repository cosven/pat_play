# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        2 1 3 4
        """
        if head is None or head.next is None:
            return head

        current_head = head.next
        current_tail = head
        current_tail.next = head.next.next
        current_head.next = current_tail

        while (current_tail.next is not None and
               current_tail.next.next is not None):
            head = current_tail.next
            tail = current_tail.next.next

            tmp = tail.next
            head.next = tmp
            tail.next = head

            current_tail.next = tail
            current_tail = head

            if current_tail.next is None:
                break

        return current_head
