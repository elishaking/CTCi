from linked_list import LinkedList, Node


def remove_dups(s_list: LinkedList):
    lookup = {}
    current_node = s_list.head

    while current_node:
        if lookup.get(current_node.value):
            temp_node = current_node
            current_node = current_node.next
            s_list.delete(temp_node)
        else:
            lookup[current_node.value] = True
            current_node = current_node.next

    return s_list


if __name__ == "__main__":
    l = LinkedList(Node(10))
    l.push(5).push(3).push(2).push(5).push(3).push(10)
    print(l)
    print(remove_dups(l))
