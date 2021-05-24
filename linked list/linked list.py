class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('index is not valid')
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        counter = 0
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            counter += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception('index is inc=valid')
        if index==0:
            self.insert_at_begning(data)

        count= 0
        itr= self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr= itr.next
            count+= 1

    def insert_after_value(self, data_after, data_to_insert):

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
    def remove_by_value(self, data):

        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
            count += 1
            itr=itr.next


ll = Linked_list()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
ll.insert_values(["banana","mango","grapes","orange",'kela'])
ll.insert_after_value("banana","apple")
ll.print()