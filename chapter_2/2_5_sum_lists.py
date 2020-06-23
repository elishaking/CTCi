from linked_list import LinkedList


# Time complexity: O(N), N represents the length of the smaller linked list
# Space complexity: O(1)
# TODO: review implementation ===> achieves constant space by mutating one of the lists
def sum_lists(list_1, list_2):
    if list_1.length > list_2.length:
        bigger = list_1
        smaller = list_2
    else:
        bigger = list_2
        smaller = list_1

    bigger_node = bigger.head
    smaller_node = smaller.head
    sum_val = 0
    car_val = 0

    while smaller_node:
        sum_val = smaller_node.value + bigger_node.value + car_val
        if sum_val > 9:
            car_val = 1
            sum_val %= 10
        else:
            car_val = 0

        bigger_node.value = sum_val

        smaller_node = smaller_node.next
        bigger_node = bigger_node.next

    if car_val != 0:
        if not bigger_node:
            bigger.push(0)
            bigger_node = bigger.tail

        bigger_node.value += car_val

    return bigger


# Time complexity: O(N), N represents the length of the smaller linked list
# Space complexity: O(1)
def sum_lists_reverse(list_1: LinkedList, list_2: LinkedList):
    return sum_lists(list_1.reverse(), list_2.reverse())


# Time complexity: O(N)
# Space complexity: O(N)
def get_number(s_list: LinkedList):
    num = ''
    current_node = s_list.head

    while current_node:
        num = str(current_node.value) + num

        current_node = current_node.next

    return int(num)


# Time complexity: O(N+M)
# Space complexity: O(N+M)
def sum_lists2(list_1, list_2):
    num1 = get_number(list_1)
    num2 = get_number(list_2)
    sum = num1 + num2
    values = list(str(sum))
    res_list = LinkedList()

    for value in values:
        res_list.unshift(int(value))

    return res_list


if __name__ == "__main__":
    l1 = LinkedList.from_list([7, 1, 6])
    l2 = LinkedList.from_list([5, 9, 2])

    print(sum_lists(l1, l2))

    li1 = LinkedList.from_list([6, 1, 7])
    li2 = LinkedList.from_list([2, 9, 5])
    print(sum_lists_reverse(li1, li2))
