"""
Module with stack implementation.
"""


class Stack:
    """ Class for stack representation. """

    def __init__(self):
        """
        Creates new stack

        :return: NoneType.
        """
        self.node = None

    def push(self, item):
        """
        Adds item to stack.

        :param item: item to add.
        :return: NoneType.
        """
        self.node = Node(item, self.node)

    def pop(self):
        """
        Return and remove
        last item from the stack.

        :return: object.
        """
        item = self.node.item
        self.node = self.node.next
        return item

    def empty(self):
        """
        Return True if stack is empty,
        False otherwise.

        :return: bool.
        """
        if self.node is None:
            return True
        return False


class Node:
    """ Class for node representation. """

    def __init__(self, item, next=None):
        """
        Create new node.

        :param item: item to be assigned to node.
        :param next: next node.
        :return: NoneType.
        """
        self.item = item
        self.next = next
