class reverse_iter:
    def __init__(self, data):
        self.collection = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.collection[self.index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
