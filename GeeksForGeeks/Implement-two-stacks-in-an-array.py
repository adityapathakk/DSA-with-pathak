# Link to problem: https://www.geeksforgeeks.org/problems/implement-two-stacks-in-an-array/1

class TwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # function to push an integer into stack 1
    def push1(self, x):
        self.stack1.append(x)

    # function to push an integer into stack 2
    def push2(self, x):
        self.stack2.append(x)

    # function to remove an element from top of stack 1
    def pop1(self):
        if self.stack1:
            return self.stack1.pop()
        else:
            return -1

    # function to remove an element from top of stack 2
    def pop2(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1