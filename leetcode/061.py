from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        if k == 0:
            return head

        i = 1

        # 1 2 . . k . .
        # x x x x x x x
        #
        # when p_right = k + 1
        #   p_left = head
        # => when p_right = end
        #   p_left = TARGET
        p_left = None
        p_right = head
        while i <= k:
            if p_right.next is not None:
                p_right = p_right.next
                i += 1
            else:
                break

        # No matter how many times it rotates.
        if i == 1:
            return head

        if i > k:
            assert i == k+1
            p_left, p_right = self.find_target(head, p_right)
            new_head = p_left.next
            p_right.next = head
            p_left.next = None
            return new_head

        return self.rotateRight(head, k % i)

    def find_target(self, p_left, p_right):
        while True:
            n = p_right.next
            if n is not None:
                p_left = p_left.next
                p_right = n
            else:
                break
        return p_left, p_right
