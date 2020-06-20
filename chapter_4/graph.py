class BSTNode:
    def __init__(self, value=0, left: BSTNode = None, right: BSTNode = None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root_value=0):
        self.root = BSTNode(root_value)

    def insert(self, value=0):
        current_node = self.root

        while current_node:
            if current_node.value < value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BSTNode(value)
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(value)
