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