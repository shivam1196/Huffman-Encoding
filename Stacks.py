from NodeInfo import NodeInfo
from StackNode import StackNode


class Stacks:
    def __init__(self):
        self.head = None
        self.capacity = 0

    def push(self, node):
        self.capacity = self.capacity + 1
        if self.head is None:
            self.head = StackNode(node)

        else:
            temp = self.head

            self.head = StackNode(node)

            self.head.next = temp


    def pop(self):
        self.capacity = self.capacity - 1
        if self.capacity > 0 :
            temp = self.head
            self.head = self.head.next

            return temp
        else:
            return None

    def peek(self):
        return self.head
