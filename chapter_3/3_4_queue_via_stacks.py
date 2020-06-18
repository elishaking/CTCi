from stack import Stack


class MyQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    # Time complexity: O(1)
    # Space complexity: O(1)
    def add(self, value=0):
        self.stack_1.push(value)

        return self

    # Time complexity: O(1) or O(N)
    # Space complexity: O(1)
    def remove(self):
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

            return self.stack_2.pop()

        else:
            return self.stack_2.pop()


if __name__ == "__main__":
    q = MyQueue().add(10).add(11).add(12).add(13).add(14).add(15)

    print(q.remove())
    print(q.remove())
    print(q.remove())
