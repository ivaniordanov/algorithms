
def memoize(key_transform):
    def decorator(function):
        def wrapper(*args, **kwargs):
            key = key_transform(*args, **kwargs)
            return cache[key] if key in cache else record(key, function(*args, **kwargs))
        cache = {}
        def record(key, result):
            cache[key] = result
            return result
        return wrapper
    return decorator

def identity(x):
    return x

@memoize(identity)
def fibonacci(n):
    return 1 if n < 2 else fibonacci(n-1) + fibonacci(n-2)
