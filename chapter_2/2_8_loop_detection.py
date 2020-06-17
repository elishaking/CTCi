from linked_list import LinkedList, Node


# Time complexity: O(N)
# Space complexity: O(N)
def loop_detection(c_list: LinkedList):
    lookup = {}
    current_node = c_list.head

    while current_node:
        node_id = id(current_node)
        if lookup.get(node_id):
            return lookup[node_id]
        else:
            lookup[node_id] = current_node

        current_node = current_node.next

    return


if __name__ == "__main__":
    node_1 = Node(10)
    node_2 = Node(30, next=node_1)
    l1 = LinkedList().push(10).push(None, node_1).push(50).push(None, node_2)
    l2 = LinkedList().push(None, node_1).push(
        100).push(300).push(None, node_2)

    print(loop_detection(l1).value)
    print(loop_detection(l2).value)
