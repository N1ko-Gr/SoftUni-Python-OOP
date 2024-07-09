def print_upper_part(number):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))



def print_lower_part(number):
    for i in range(n):
        print(' ' * (i + 1) + '* ' * (n - i - 1))


n = int(input())

print_upper_part(n)
print_lower_part(n)