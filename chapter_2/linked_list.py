class Node:
    def __init__(self, value=0, next: Node = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None, tail: Node = None):
        self.head = head
        self.tail = tail

    def push(self, value: int):
        new_node = Node(value=value)
        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def unshift(self, value: int):
        new_node = Node(value=value, next=self.head)
        self.head = new_node

        return new_node

    def insert(self, value: int, index: int):
        current_node = self.head
        current_index = 0

        if index == 0:
            return self.unshift(value)

        while current_node:
            if current_index == index - 1:
                new_node = Node(value=value, next=current_node.next)
                current_node.next = new_node

                return new_node

            current_index += 1
            current_node = current_node.next

        return None
