# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        tail = head
        while tail.next is not None:
            tail = tail.next

        while True:
            tail_next = tail.next
            tail.next = head
            head_next = head.next
            head.next = tail_next
            head = head_next

            if head is tail:
                break

        return tail
