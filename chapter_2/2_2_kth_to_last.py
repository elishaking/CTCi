from linked_list import LinkedList, Node


# Time complexity: O(N)
# Space complexity: O(1)
def kth_to_last(s_list: LinkedList, k: int):
    runner_node = s_list.head
    current_node = runner_node
    pos = 0

    while pos < k:
        runner_node = runner_node.next
        pos += 1

        if not runner_node:
            raise Exception('index out of range')

    while runner_node:
        runner_node = runner_node.next
        current_node = current_node.next

    return current_node.value


if __name__ == "__main__":
    l = LinkedList(Node(10))
    l.push(5).push(3).push(2).push(5).push(3).push(10)
    print(l)
    print(kth_to_last(l, 3))
