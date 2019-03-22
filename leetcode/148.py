# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        s = ''
        while node is not None:
            s += str(node.val)
            node = node.next
            if node is not None:
                s += '->'
        return s


def sort(l):
    if l is None or l.next is None:
        return l, l

    hl_head = hl_tail = ListNode(None)
    mid_head = mid_tail = l
    hr_head = hr_tail = ListNode(None)

    l = l.next
    while l is not None:
        lnext = l.next
        if l.val < mid_head.val:
            hl_tail.next = l
            hl_tail = l
        elif l.val == mid_head.val:
            mid_tail.next = l
            mid_tail = l
        else:
            hr_tail.next = l
            hr_tail = l
        l.next = None
        l = lnext

    mid_tail.next = None

    if hl_head.next is not None:
        head, ltail = sort(hl_head.next)
    else:
        head = ltail = None
    if ltail is not None:
        ltail.next = mid_head
    else:
        head = ltail = mid_head

    if hr_head.next is not None:
        mid_tail.next, rtail = sort(hr_head.next)
    else:
        rtail = mid_tail
    return head, rtail


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        head, _ = sort(head)
        return head


if __name__ == '__main__':
    t5 = ListNode(5)
    t4 = ListNode(4)
    t3 = ListNode(3)
    t2 = ListNode(2)
    t1 = ListNode(1)

    t5.next = t4
    t4.next = t3
    t3.next = t1
    t1.next = t2

    print(Solution().sortList(t5))
