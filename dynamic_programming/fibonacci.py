import memoize

def identity(x):
    return x

@memoize(identity)
def fibonacci(n):
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)
