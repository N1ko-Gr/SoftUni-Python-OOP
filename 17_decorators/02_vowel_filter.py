def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = 'aeiouy'
        return [i for i in result if i in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
