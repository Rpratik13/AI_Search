class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")

        return self.stack.pop()
