class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration

        result = self.current
        self.current += self.step
        self.index += 1
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
