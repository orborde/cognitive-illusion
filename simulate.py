# Simulate a "choice" between which of the premises to enforce as actual rules.

C_1A = "1a"
C_1B = "1b"
CHOICES = set([C_1A, C_1B])

UNKNOWN = "(unknown)"

def simulate(K, C):
    assert C in CHOICES

    A = UNKNOWN
    if C is C_1A:
        if K:
            A = True
    if C is C_1B:
        if not K:
            A = True

    return K, A

import itertools

print '=== TRUTH TABLE ==='
for K, C in itertools.product([True, False], CHOICES):
    print K, C, '->', simulate(K, C)
print

print '=== ORIGINAL PUZZLE ==='
print 'Given that one and only one of the rules applies, and that you have a King,',
print 'the implications of different rules applying are:'

possibilities = set()
for C in CHOICES:
    _, result = simulate(True, C)
    print C, 'true: A =', result
    possibilities.add(result)

print 'Therefore, the possible values of A are:',
print '[', ', '.join(map(str, possibilities)), ']'
