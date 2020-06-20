class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = self.head

    def push(self, value: int, node: Node = None):
        if node:
            new_node = node
        else:
            new_node = Node(value=value)

        if self.head == None:
            self.head = new_node
            self.tail = self.head

            return self

        self.tail.next = new_node
        self.tail = new_node

        return self

    def unshift(self, value: int):
        new_node = Node(value=value, next=self.head)
        self.head = new_node

        return self

    def shift(self):
        node = self.head
        self.head = self.head.next

        return node

    def insert(self, value: int, index: int):
        current_node = self.head
        current_index = 0

        if index == 0:
            return self.unshift(value)

        while current_node:
            if current_index == index - 1:
                new_node = Node(value=value, next=current_node.next)
                current_node.next = new_node

                return self

            current_index += 1
            current_node = current_node.next

        raise Exception('index out of range')

    def delete(self, node: Node):
        if node == self.head:
            temp_node = self.head
            self.head = self.head.next
            del temp_node

        prev_node = self.head
        current_node = self.head.next

        while current_node:
            if node == current_node:
                prev_node.next = current_node.next
                del current_node

                return self

            prev_node = prev_node.next
            current_node = current_node.next

        return self

    def __str__(self):
        values = []
        current_node = self.head

        while current_node:
            values.append(current_node.value)
            current_node = current_node.next

        return str(values)


class Queue:
    def __init__(self):
        self.values = LinkedList()

    def add(self, value):
        self.values.push(value)
        return self

    def remove(self):
        return self.values.shift()

    def peek(self):
        return self.values.head.value

    def is_empty(self):
        return self.values.head == None

    def __str__(self):
        return str(self.values)
