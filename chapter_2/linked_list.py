class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.tail = self.head
        self.length = 0
        if head:
            self.length += 1

    @classmethod
    def from_list(self, values: list):
        l_list = LinkedList()

        for value in values:
            l_list.push(value)

        return l_list

    def push(self, value: int, node: Node = None):
        if node:
            new_node = node
        else:
            new_node = Node(value=value)

        self.length += 1

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

        self.length += 1

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
                self.length += 1

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
                self.length -= 1

                return self

            prev_node = prev_node.next
            current_node = current_node.next

        raise Exception('node does not exist')

    def reverse(self):
        current_node = self.head
        next_node = current_node.next
        current_node.next = None

        while next_node:
            temp_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = temp_node

        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node

        return self

    def __str__(self):
        values = []
        current_node = self.head

        while current_node:
            values.append(current_node.value)
            current_node = current_node.next

        return str(values)

    def __eq__(self, other):
        if self.length != other.length:
            return False

        current_node = self.head
        other_node = other.head

        while current_node:
            if current_node.value != other_node.value:
                return False

            current_node = current_node.next
            other_node = other_node.next

        return True


if __name__ == "__main__":
    l = LinkedList(Node(10))
    l.push(5).push(3).push(2)

    print(l)

    node_to_delete = l.head.next
    print(node_to_delete.value)
    l.delete(node_to_delete)
    print(l)

    l2 = LinkedList.from_list([1, 2, 3, 4, 5])
    print(l2)
    print(l2.length)
    print(l2.reverse())

    print(l2 == LinkedList.from_list([5, 4, 3, 2, 1]))
