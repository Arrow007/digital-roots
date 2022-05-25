def digital_root(n, base = 10):
    if n == 0:
        return n
    elif n != 0:
        dr = 1 + ((n - 1) % (base - 1))
        return dr
