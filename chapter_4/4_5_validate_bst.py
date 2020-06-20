from graph import BSTNode, BinarySearchTree


# Time complexity: O(N)
# Space complexity: O(N)
def validate_bst(node: BSTNode):
    left = True
    right = True

    if node.right and node.left and node.right.value < node.left.value:
        return False
    if node.right:
        right = validate_bst(node.right)
    if node.left:
        left = validate_bst(node.left)

    return left and right


if __name__ == "__main__":
    bst = BinarySearchTree(2).insert(1).insert(3).insert(5).insert(2)
    print(validate_bst(bst.root))
