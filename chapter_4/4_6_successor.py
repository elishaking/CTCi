import unittest


class BSTNodeP:
    def __init__(self, value=0, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.value)


class BSTP:
    def __init__(self, root_value=0):
        self.root = BSTNodeP(root_value)

    def insert(self, value=0):
        current_node = self.root

        while current_node:
            if current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNodeP(value, current_node)
                    return self
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNodeP(value, current_node)
                    return self


def successor(node: BSTNodeP):
    result: BSTNodeP = None

    if node.right:
        # get left-most child of right sub-tree
        result = node.right
        while result.left:
            result = node.left
    elif node.parent:
        current_node = node
        while current_node.parent and not result:
            if current_node.parent.left == current_node:
                result = current_node.parent

            current_node = current_node.parent

    return result


class Tests(unittest.TestCase):
    def test_successor(self):
        bstp = BSTP(10).insert(5).insert(12).insert(6).insert(4)
        test_node_1 = bstp.root.left
        test_node_2 = bstp.root.left.right
        test_node_3 = bstp.root.right
        self.assertEqual(successor(test_node_1).value, 6)
        self.assertEqual(successor(test_node_2).value, 10)
        self.assertEqual(successor(test_node_3), None)


if __name__ == "__main__":
    unittest.main()
