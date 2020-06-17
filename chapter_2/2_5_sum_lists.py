from linked_list import LinkedList, Node


def get_number(s_list: LinkedList):
    num = ''
    current_node = s_list.head

    while current_node:
        num = str(current_node.value) + num

        current_node = current_node.next

    return int(num)


def sum_lists(list_1, list_2):
    num1 = get_number(list_1)
    num2 = get_number(list_2)
    sum = num1 + num2
    values = list(str(sum))
    res_list = LinkedList()

    for value in values:
        res_list.unshift(int(value))

    return res_list


if __name__ == "__main__":
    l1 = LinkedList(Node(7)).push(1).push(6)
    l2 = LinkedList(Node(5)).push(9).push(2)

    print(sum_lists(l1, l2))
