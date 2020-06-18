class Stack:
    def __init__(self):
        self.values = []

    def push(self, value=0):
        self.values.append(value)

        return self

    def pop(self):
        if len(self.values) == 0:
            raise Exception('Stack is empty')

        return self.values.pop()

    def peek(self):
        return self.values[-1]

    def is_empty(self):
        return len(self.values) == 0

    def __str__(self):
        return str(self.values)


if __name__ == "__main__":
    s = Stack().push(10).push(20).push(2).push(30).push(3)
    print(s)
    print(s.peek())
    print(s.is_empty())
