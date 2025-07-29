# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        p1 = head
        p2 = head

        while True:
            if p1 is None or p2 is None:
                return False

            p2_next = p2.next
            p1_next = p1.next
            if p2_next is None or p1_next is None:
                return False

            p1 = p1_next
            p2 = p2_next.next

            if p1 == p2:
                return True
