from linked_list import LinkedList, Node


def kth_to_last(s_list: LinkedList, k: int):
    pos = 0
    current_node = s_list.head

    while True:
        if pos == k:
            break

        current_node = current_node.next
        if current_node == None:
            raise Exception('k is out of range')

        pos += 1

    values = []
    while current_node:
        values.append(current_node.value)
        current_node = current_node.next

    return values


if __name__ == "__main__":
    l = LinkedList(Node(10))
    l.push(5).push(3).push(2).push(5).push(3).push(10)
    print(l)
    print(kth_to_last(l, 3))
