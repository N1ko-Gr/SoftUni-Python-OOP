def possible_permutations(ls):
    if len(ls) == 0:
        yield []
    else:
        for i in range(len(ls)):
            for perm in possible_permutations(ls[:i] + ls[i+1:]):
                yield [ls[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
