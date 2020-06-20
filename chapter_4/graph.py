from queue import Queue


class BSTNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


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
                    return self
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BSTNode(value)
                    return self

    def __str__(self):
        queue = Queue()
        queue.add(self.root)
        values = []

        while not queue.is_empty():
            exp = queue.remove()
            values.append(str(exp.value))

            if exp.value.right:
                queue.add(exp.value.right)
            if exp.value.left:
                queue.add(exp.value.left)

        return str(values)


if __name__ == "__main__":
    bst = BinarySearchTree(2).insert(1).insert(3)
    print(bst)
