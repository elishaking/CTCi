from linked_list import LinkedList, Node


# Time complexity: O(N), N represents the length of the larger linkedlist
# Space complexity: O(1)
def intersection(list_1: LinkedList, list_2: LinkedList):
    if list_1.length > list_2.length:
        bigger = list_1
        smaller = list_2
    else:
        bigger = list_2
        smaller = list_1

    bigger_node = bigger.head
    smaller_node = smaller.head
    diff = bigger.length - smaller.length

    while diff > 0:
        bigger_node = bigger_node.next
        diff -= 1

    while bigger_node:
        if bigger_node.value == smaller_node.value:
            return True

        bigger_node = bigger_node.next
        smaller_node = smaller_node.next

    return False


# Time complexity: O(N+M)
# Space complexity: O(N)
def intersection_old(list_1: LinkedList, list_2: LinkedList):
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
    l1 = LinkedList.from_list([1, 2, 3, 4, 5])
    l2 = LinkedList.from_list([3, 4, 5])
    print(intersection(l1, l2))

    # remove intersecting node from l2
    l2 = LinkedList.from_list([100, 200, 300])
    print(intersection(l1, l2))
