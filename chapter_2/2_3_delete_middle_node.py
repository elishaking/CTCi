from linked_list import LinkedList, Node


def delete_middle_node(s_list: LinkedList, node: Node):
    s_list.delete(node)


if __name__ == "__main__":
    l = LinkedList(Node(10)).push(5).push(300).push(2).push(5).push(3).push(10)
    print(l)
    node_to_delete = l.head.next.next
    print(node_to_delete.value)
    delete_middle_node(l, node_to_delete)
    print(l)
