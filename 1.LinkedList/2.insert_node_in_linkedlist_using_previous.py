class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        current = self.head
        previous = None
        while current and current.data < data:
            previous = current
            current = current.next
        if previous is None:
            new_node.next = self.head
            self.head = new_node
        else:
            previous.next = new_node
            new_node.next = current