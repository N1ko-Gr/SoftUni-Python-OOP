class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.sorted_vowels = [x for x in self.string if x.lower() in self.vowels]


    def __iter__(self):
        return self

    def __next__(self):
        if not self.sorted_vowels:
            raise StopIteration
        return self.sorted_vowels.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
