
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        """ Store the data, and set next to None"""

    def __str__(self):
        return str(self.data)
        """ Return a string representation of the data """


class Storage:
    def __init__(self, head=None):
        self.head = head
        """ Creates an empty Storage class. Sets head to None. """

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        """ Create a Node to hold the data, then put it at the head of the list. """

    def pop(self):
        if self.head == None:
            return
        removed_head_data = self.head.data
        self.head = self.head.next
        return removed_head_data

        """ Remove the head Node and return its data. """

    def peek(self):
        return self.head.data
        """ Return the data from the head Node, without removing it. """

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
        """ Return True if the list is empty, otherwise False """
