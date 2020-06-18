from stack import Stack


# Time complexity: O(N^2)
# Space complexity: O(N)
def sort_stack(stack: Stack):
    sorted_stack = Stack()

    while not stack.is_empty():
        value = stack.pop()
        pops = 0
        while not sorted_stack.is_empty() and sorted_stack.peek() < value:
            stack.push(sorted_stack.pop())
            pops += 1

        sorted_stack.push(value)

        while pops > 0:
            sorted_stack.push(stack.pop())
            pops -= 1

    return sorted_stack


if __name__ == "__main__":
    s = Stack().push(10).push(20).push(2).push(30).push(3)
    print(s)
    sorted_stack = sort_stack(s)
    print(sorted_stack)
