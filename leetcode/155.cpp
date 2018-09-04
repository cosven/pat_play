/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

-------------------------
-------------------------
-------------------------

- use two stack to implement a min stack

其他常见思路：

1. 容易想到最小堆，但是最小堆的时间复杂度不是常数

容易出错的地方：

1. push 一个值的时候，如果新的值 == 老的 min 值，也要 push 到 s2 里头

*/


class MinStack {

public:
    /** initialize your data structure here. */
    stack<int> s1;  // store all values
    stack<int> s2;  // to store min values
    
    void push(int x) {
        s1.push(x);  
        if (s2.empty())
            s2.push(x);
        else if (x <= getMin())
            s2.push(x);
    }
    
    void pop() {
        if (top() == s2.top())
            s2.pop();
        s1.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return s2.top();
    }
};
