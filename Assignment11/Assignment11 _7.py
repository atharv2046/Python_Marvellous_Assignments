def print_pattern(n, i=1):
    if i > n:
        return
    print("* " * i)
    print_pattern(n, i + 1)

print(print_pattern(3))

