# Stacks and Queues:
# Implement a stack using two queues.

from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        self.queue1.append(value)

        # Move all elements from queue2 to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        # Swap the names of the queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if not self.queue2:
            return None
        return self.queue2.popleft()


# Implement a queue using two stacks.

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            # Move all elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2.pop()


# Write a program to check if a given string of parentheses is balanced.
def is_balanced_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack
