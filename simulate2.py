# Model the situation with formal logic.

def ifthen(x, y):
    """
    >>> ifthen(True, False)
    False
    >>> ifthen(True, True)
    True
    >>> ifthen(False, False)
    True
    >>> ifthen(False, True)
    True
    """
    if not x:
        return True
    else:
        return y

def is_the_thing(K, A):
    p1a = ifthen(    K, A)
    p1b = ifthen(not K, A)
    p2  = K

    return (p1a ^ p1b) and p2

def show(K, A):
    out = '('
    if not K: out += '!'
    out += 'K,'
    if not A: out += '!'
    out += 'A)'
    return out

import doctest
import itertools

fails, _ = doctest.testmod()
assert fails == 0


print '=== TRUTH TABLE ==='
valid = set()
for K, A in itertools.product([False, True], repeat=2):
    result = is_the_thing(K, A)
    print show(K, A), '->', result
    if result:
        valid.add( (K,A) )

print '=== VALID RESULTS ==='
for K, A in valid:
    print show(K, A)
