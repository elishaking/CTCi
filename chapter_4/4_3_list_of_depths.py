from queue import Queue, LinkedList
from graph import BinarySearchTree


# Time complexity: O(N)
# Space complexity: O(N)
def list_of_depths(bt: BinarySearchTree):
    nodes = {}
    que = Queue()
    que.add([bt.root, 1])

    while not que.is_empty():
        (node, pos) = que.remove().value

        if not nodes.get(pos):
            nodes[pos] = LinkedList()

        nodes[pos].unshift(node.value)

        if node.left:
            que.add([node.left, pos + 1])
        if node.right:
            que.add([node.right, pos + 1])

    return nodes


# TODO: implement the above with DFS


if __name__ == "__main__":
    bst = BinarySearchTree(2).insert(1).insert(3).insert(5).insert(2)
    print(list_of_depths(bst))
