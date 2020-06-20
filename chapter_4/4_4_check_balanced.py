from graph import BSTNode, BinarySearchTree


# Time complexity: O(N)
# Space complexity: O(N) ---> recursive calls
def height(node: BSTNode, h: int):
    left = 0
    right = 0
    if node.left:
        left = height(node.left, h + 1) + h
    if node.right:
        right = height(node.right, h + 1) + h

    if left > right:
        return left
    else:
        return right


# Time complexity: O(N)
# Space complexity: O(N)
def check_balanced(bst: BinarySearchTree):
    root = bst.root

    if not root:
        return True

    left = height(root.left, 1)
    right = height(root.right, 1)

    if abs(left - right) > 1:
        return False

    return True


if __name__ == "__main__":
    bst = BinarySearchTree(2).insert(1).insert(3).insert(4).insert(5)
    print(check_balanced(bst))
