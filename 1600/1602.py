def ABS(n):
    return -n if n < 0 else n

n_input = input()
n = float(n_input) if '.' in n_input else int(n_input)


print(ABS(n))
