import math
import itertools

def exponent(x):
    return math.e ** x

def split(sequence):
    return [sequence[::2],sequence[1::2]]

def power_range(constant, n):
    return (constant**i for i in range(n))

def unity_circle(n, coefficient):
    return power_range(exponent(complex(0, coefficient * math.pi / (n * abs(coefficient)))), n)

def array_pad(arr, n, value=0):
    return arr + [value] * n

def combine(A, B, coefficient):
  n = len(A)
  result = [0] * n * 2
  for i, (a,b, omega) in enumerate(zip(A, B, unity_circle(n, coefficient))):
    result[i], result[i + n] = a + (omega * b), a - (omega * b)
  return result

def IFFT(X):
    return [float(a.real) / len(X) for a in FFT(X, -1)]

def FFT(X, coefficient=1):
    assert math.log2(len(X)) % 1 == 0, "Must be power of 2"
    return X if len(X) == 1 else combine(*[FFT(part, coefficient) for part in split(X)], coefficient)

def multiply(A, B):
    return IFFT([x*y for x, y in zip(FFT(array_pad(A, len(B))), FFT(array_pad(B, len(A))))])

print (multiply(list(range(8)), list(range(8))))
