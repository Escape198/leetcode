class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        if node is self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node is self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = node.next = None

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current

    def display(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()  # 1 2 3
node = dll.find(2)
dll.delete(node)
dll.display()  # 1 3
dll.prepend(0)
dll.display()  # 0
