import math
from linked_list import LinkedList, Node


# Time complexity: O(N)
# Space complexity: O(N)
def palindrome(s_list: LinkedList):
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
