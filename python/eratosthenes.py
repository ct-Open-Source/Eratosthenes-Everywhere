#!/usr/bin/env python3

import struct 

def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

def main():
    prime = primes()
    for _ in range(10_000):
        print(next(prime), end=' ')

if __name__ == '__main__':
    main()
