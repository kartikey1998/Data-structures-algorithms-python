from collections import deque
class queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def dequeue(self):
        self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) ==0
    def size(self):
        return len(self.buffer)