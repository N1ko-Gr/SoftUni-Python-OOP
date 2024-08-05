def squares(n):
    curr = 1
    while curr <= n:
        yield curr ** 2
        curr += 1




print(list(squares(5)))