from chapter_2.linked_list import LinkedList, Node


def remove_dups(s_list: LinkedList):
    lookup = {}
    current_node = s_list.head

    while current_node:
        if lookup[current_node.value]:
            # TODO: delete
            pass
        else:
            lookup[current_node.value] = True

    return s_list
