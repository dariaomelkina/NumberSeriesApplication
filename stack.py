class Stack:
    def __init__(self):
        self.node = None

    def push(self, item):
        self.node = Node(item, self.node)

    def pop(self):
        item = self.node.item
        self.node = self.node.next
        return item

    def empty(self):
        if self.node is None:
            return True
        return False



class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
