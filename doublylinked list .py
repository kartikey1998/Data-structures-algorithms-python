class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list():
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head= node

    def print_f(self):
        if self.head==None:
            print("linked list is empty")
            return

        itr = self.head
        while itr:
            print(itr.data, end='--->')
            itr = itr.next
        print('')

    def print_b(self):
        lastnode = self.get_last_node()
        itr = lastnode
        while itr:
            print(itr.data, end='--->')
            itr = itr.prev
        print('')

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data,None, None)
            self.head = node

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

dll = doubly_linked_list()
dll.insert_at_begining('banana')
dll.insert_at_begining('apple')
dll.insert_at_begining('chiku')
dll.print_f()
dll.insert_at_end('kela')
dll.insert_at_end('59')
dll.insert_at_end(60)
dll.print_f()
dll.print_b()