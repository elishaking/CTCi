from linked_list import LinkedList, Node


def intersection(list_1: LinkedList, list_2: LinkedList):
    lookup_1 = {}
    current_node = list_1.head

    while current_node:
        lookup_1[id(current_node)] = True
        current_node = current_node.next

    current_node = list_2.head

    while current_node:
        if lookup_1.get(id(current_node)):
            return True

        current_node = current_node.next

    return False


if __name__ == "__main__":
    common_node = Node(10)
    l1 = LinkedList().push(10).push(20).push(None, common_node).push(50)
    l2 = LinkedList().push(200).push(None, common_node).push(100).push(300)
    print(intersection(l1, l2))

    # remove intersecting node from l2
    l2 = LinkedList().push(200).push(100).push(300)
    print(intersection(l1, l2))
