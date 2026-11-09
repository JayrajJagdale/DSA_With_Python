def fibbo(n):
    if n == 0 or n == 1:
        return n
    return fibbo(n-1) + fibbo(n-2)

print(fibbo(4))