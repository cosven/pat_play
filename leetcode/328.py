# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next

        odd_head = ListNode(0, head)
        even_head = ListNode(0, even)

        while odd is not None and even is not None:
            odd.next = even.next

            if even.next is not None:
                odd = even.next
                even.next = odd.next
                even = odd.next
            else:
                even = None

        odd.next = even_head.next
        return odd_head.next


