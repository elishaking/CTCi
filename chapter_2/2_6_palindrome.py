import math
from linked_list import LinkedList, Node


# Time complexity: O(N)
# Space complexity: O(N)
def palindrome(s_list: LinkedList):
    current_node = s_list.head
    new_list = LinkedList()

    while current_node:
        new_list.unshift(current_node.value)
        current_node = current_node.next

    return new_list == s_list


# Time complexity: O(N)
# Space complexity: O(N)
def palindrome_2(s_list: LinkedList):
    chars = []
    current_node = s_list.head

    while current_node:
        chars.append(current_node.value)
        current_node = current_node.next

    left = 0
    right = len(chars) - 1
    while right > left:
        if chars[right] != chars[left]:
            return False

        right -= 1
        left += 1

    return True


if __name__ == "__main__":
    s1 = LinkedList().push('l').push('e').push('v').push('e').push('l')
    s2 = LinkedList().push('l').push('e').push('v').push('f').push('l')
    print(palindrome(s1))
    print(palindrome(s2))
