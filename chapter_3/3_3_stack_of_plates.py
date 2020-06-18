class SetOfStacks:
    def __init__(self, max=3):
        self.max = max
        self.values = []

    def push(self, value=0):
        self.values.append(value)

        return self

    def pop(self):
        if len(self.values) == 0:
            raise Exception('Stack is empty')

        return self.values.pop()

    # Time complexity: O(1)
    # Space complexity: O(1)
    def pop_at(self, index):
        start_index = index * self.max
        if start_index >= len(self.values):
            raise Exception('Sub stack at index: ' +
                            str(index) + ' does not exist')

        pop_index = start_index + self.max - 1
        if pop_index > len(self.values):
            pop_index = len(self.values) - 1

        value = self.values.pop(pop_index)

        return value

    def __str__(self):
        return str(self.values)


if __name__ == "__main__":
    stacks = SetOfStacks(2)
    stacks.push(10).push(3).push(9).push(15).push(14).push(11).push(100)
    print(stacks)
    stacks.pop_at(1)
    stacks.pop_at(1)
    print(stacks)


class SetOfStacks_2:
    def __init__(self, max=3):
        self.max = max
        self.values = [[]]
        self.current_stack = 0

    def push(self, value=0):
        if len(self.values[self.current_stack]) >= self.max:
            self.current_stack += 1
            self.values.append([])

        self.values[self.current_stack].append(value)

        return self

    def pop(self):
        if len(self.values[self.current_stack]) == 0:
            self.current_stack -= 1
            self.values.pop()

            if len(self.values) == 0:
                raise Exception('Stack is empty')

        return self.values[self.current_stack].pop()

    def pop_at(self, index):
        if index >= len(self.values):
            raise Exception('Sub stack at index: ' +
                            str(index) + ' does not exist')

        value = self.values[index].pop()

        if len(self.values[index]) == 0:
            self.values.pop(index)
            self.current_stack -= 1

        return value

    def __str__(self):
        return str(self.values)
