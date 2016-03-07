#include<stdio.h>
#include<stdlib.h>
#include<math.h>


/*
 * 不正确的版本，对一些情况没有考虑到，具体可以参考 github issues
 * */

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    if (!l1) return l2;
    if (!l2) return l1;
    int num1 = 0;
    int count = 0;
    while (l1){
        num1 += l1->val * pow(10, count);
        count ++;
        l1 = l1->next;
    }

    int num2 = 0;
    int count2 = 0;
    while (l2){
        num2 += l2->val * pow(10, count2);
        count2 ++;
        l2 = l2->next;
    }
    // printf("num1: %d, num2: %d\n", num1, num2);
    
    struct ListNode *result = (struct ListNode *)calloc(1, sizeof(struct ListNode));
    struct ListNode *head = (struct ListNode *)calloc(1, sizeof(struct ListNode));
    int num = num1 + num2;
    int count3 = 1;
    int remainder = num % 10;
    int quotient = num / 10;
    result->val = remainder;
    result->next = NULL;
    head = result;
    // printf("head val : %d\n", head->val);
    while ( quotient > 0){
        remainder = quotient % 10;
        quotient = quotient / 10;
        struct ListNode *tmp = (struct ListNode *)calloc(1, sizeof(struct ListNode));
        tmp->val = remainder;
        tmp->next = NULL;
        result->next = tmp;
        result = tmp;
        // printf("head val : %d\n", head->val);
        count3 ++;
    }
    return head;
}

int main(){
    struct ListNode ln;
    ln.val = 10;
    ln.next = NULL;

    struct ListNode ln2;
    ln2.val = 2;
    ln2.next = NULL;
    
    struct ListNode *result;
    result = addTwoNumbers(&ln, &ln2);
    while(result){
        printf("result val: %d", result->val);
        result = result->next;
    }
    return 0;
}
