/*
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

---------------------------
---------------------------

*/


class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL)
            return NULL;
        ListNode * tmpHeadA = headA;
        ListNode * tmpHeadB = headB;
        bool aEnd = false;
        bool bEnd = false;
        while (1){
            if (tmpHeadA == tmpHeadB)
                return tmpHeadA;
            if (tmpHeadA == NULL || tmpHeadB == NULL)
                return NULL;
            tmpHeadA = tmpHeadA->next;
            tmpHeadB = tmpHeadB->next;
            if (tmpHeadA == NULL && aEnd != true){
                tmpHeadA = headB;
                aEnd = true;
            }

            if (tmpHeadB == NULL && bEnd != true){
                tmpHeadB = headA;
                bEnd = true;
            }
        }
        return NULL;
    }
};
