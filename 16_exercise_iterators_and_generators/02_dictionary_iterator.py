class dictionary_iter:

    def __init__(self, *kwargs):
        self.dictionary = dict(*kwargs)
        self.keys = list(self.dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        self.index += 1
        return key, self.dictionary[key]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
