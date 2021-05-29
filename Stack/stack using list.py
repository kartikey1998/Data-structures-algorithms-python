class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
        else :
            print('{} is already is in stack'.format(data))

    def pop (self, data):
        if data not in self.stack:
            print("{} is invalid".format(data))

        else:
            self.stack.pop()

    def print_full_stack(self):
        print(self.stack)

    def peek(self):
        print(self.stack[-1])

    def is_empty(self):
        return len(self.stack)==0
s = Stack()
print(s.is_empty())
s.push(65)
s.push(66)
s.push(65897)
s.push(65897)
s.pop(87)
s.pop(65897)
s.peek()
s.print_full_stack()
s.is_empty()