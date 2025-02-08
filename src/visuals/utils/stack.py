import stack

class Stack:
    """
    A wrapper class for the stack module.

    TODO:
    Defines max size of the stack to be 10. This can be edited.

    """
    def __init__(self):
        self.stack = stack.Stack()

    def push(self, item):
        self.stack.push(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def is_empty(self):
        return self.stack.is_empty()

    def size(self):
        return self.stack.size()