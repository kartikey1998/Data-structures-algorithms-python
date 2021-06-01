class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last==None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next=Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head == None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
    def print_queue(self):
        itr = self.head
        while itr:
            print(itr.data, end='--->')
            itr = itr.next
        print('')

    def get_size(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count +=1

        return count


que = Queue()
que.enqueue(86)
que.enqueue(68)
que.enqueue(67)
que.enqueue(98)
que.enqueue(24)
que.enqueue('kartikey')
que.print_queue()
que.dequeue()
que.print_queue()
que.dequeue()
que.dequeue()
que.print_queue()
print(que.dequeue())
que.enqueue(2654)
que.enqueue(184)
que.enqueue(965)
que.print_queue()
print(que.get_size())