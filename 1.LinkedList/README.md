# Linkedlist
Python programming tips and tricks

![status](https://img.shields.io/badge/status-work%20in%20progress-blue?style=flat-square)

## `1` Insert node in ordered linkedlist with self.length without self.previous

This will insert the new node in a proper position in the linked list, maintaining the order.
how to do using the length of the linked list and without the previous?
To insert a node in an ordered linked list in Python without using the "previous" variable, you can use the following steps:

* `1` Create a new node with the data you want to insert.
* `2` Initialize a current node variable to the head of the list.
* `3` Initialize a counter variable to keep track of the position of the current node.
* `4` Traverse the list until you find the first node whose data is greater than the data of the new node or the counter variable reaches the length of the list.
* `5` Insert the new node before the current node.

```python
def insert(self, s):
    new_node = Node(s)
    current = self.first()
    counter = 0
    while current and current.value() < s:
        current = current.next()
        counter += 1
    if counter == 0:
        new_node.set_next(self.first())
        self.__head = new_node
    else:
        current = self.first()
        for i in range(counter - 1):
            current = current.next()
        new_node.set_next(current.next())
        current.set_next(new_node)
```

This will insert the new node in a proper position in the linked list, maintaining the order. Using the length variable could be useful in the cases that you don't have the previous reference to the node, but the trade off is that you have to traverse the linked list twice, once to get the length and other to insert the element in the right position.

Example:
Let's say we have a linked list with the following values in order: [2, 4, 7, 8, 9] and we want to insert a new node with the value 5.

 `1` Create a new node with the data 5
* `2` Initialize a current node variable to the head of the list (2)
* `3` Initialize a counter variable to keep track of the position of the current node.
* `4` Traverse the list until you find the first node whose data is greater than the data of the new node (7) or the counter variable reaches the length of the list.
* `5` Insert the new node before the current node.

The linked list after the insertion would look like this: [2, 4, 5, 7, 8, 9].

You can visualize the linked list as a chain of nodes, where each node has a value, and a reference to the next node. Each time you insert a new node, you are breaking the chain and creating a new one, where the new node points to the next node and the previous node points to the new one. The head of the list keeps pointing to the first node in the list and every time you traverse it, you are going through the chain of nodes, following the pointer next.


## `2` Insert node in ordered linkedlist with self.previous

To insert a node in an ordered linked list in Python, you can use the following steps:

* `1` Create a new node with the data you want to insert.
* `2` Initialize a current node variable to the head of the list.
* `3` Traverse the list until you find the first node whose data is greater than the data of the new node or you reach the end of the list.
* `4` Insert the new node before the current node.

```python
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
```

This will insert the new node in a proper position in the linked list, maintaining the order.