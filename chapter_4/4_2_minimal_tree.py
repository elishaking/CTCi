from graph import BinarySearchTree


# Time complexity: O(N)
# Space complexity: O(N)
def minimal_tree(arr: list):
    N = len(arr)
    mid = N // 2
    forward_1 = mid
    forward_2 = mid
    backward_1 = mid
    backward_2 = mid

    bst = BinarySearchTree(arr[mid])

    while forward_1 < N or forward_2 < N or backward_1 > -1 or backward_2 > -1:
        forward_1 += 1
        forward_2 += 2
        backward_1 -= 1
        backward_2 -= 2

        if forward_1 < N:
            bst.insert(arr[forward_1])
        if forward_2 < N:
            bst.insert(arr[forward_2])
        if backward_1 > -1:
            bst.insert(arr[backward_1])
        if backward_2 > -1:
            bst.insert(arr[backward_2])

    return bst


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(minimal_tree(arr))
