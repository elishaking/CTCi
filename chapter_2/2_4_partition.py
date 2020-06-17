from linked_list import LinkedList, Node


# Time complexity: O(N)
# Space complexity: O(N)
def partition(s_list: LinkedList, partition: int):
    greater_list = LinkedList()
    main_list = LinkedList()

    current_node = s_list.head

    while current_node:
        if current_node.value < partition:
            main_list.push(current_node.value)
        else:
            greater_list.push(current_node.value)

        current_node = current_node.next

    if main_list.head == None:
        return greater_list

    main_list.tail.next = greater_list.head
    main_list.tail = greater_list.tail

    return main_list


if __name__ == "__main__":
    l = LinkedList(Node(10)).push(5).push(300).push(2).push(5).push(3).push(10)
    print(l)
    print(partition(l, 7))
