class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = self.head

    def push(self, value: int):
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


if __name__ == "__main__":
    l = LinkedList(Node(10))
    l.push(5).push(3).push(2)

    print(l)

    node_to_delete = l.head.next
    print(node_to_delete.value)
    l.delete(node_to_delete)
    print(l)
