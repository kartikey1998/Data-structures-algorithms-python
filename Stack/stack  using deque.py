from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)


## function to reverse a string using stack
def reverse_string(string):
    stack = Stack()
    revs = ''
    for i in string:
        stack.push(i)
    while stack.size()!=0:
        revs += stack.pop()
    return revs

## function for checking if the string has balanced paranthesis
def is_match(ch1, ch2):
    dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    return dict[ch1] ==ch2

def is_balanced(string):
    stack = Stack()
    for ch in string:
        if ch=="(" or ch=="[" or ch== "{":
            stack.push(ch)
        if ch==')' or ch==']' or ch=='}':
            if stack.size()==0:
                return False
            else:
                return is_match(ch, stack.pop())
s = Stack()
print(reverse_string("We will conquere COVID-19"))

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))