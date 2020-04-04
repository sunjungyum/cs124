# https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

import random

# returns (a^b) mod n


def modExponent(a, b, n):
    result = 1
    a = a % n
    if (a == 0):
        return 0
    while (b > 0):
        if (b & 1 == 1):
            result = (result * a) % n
        b = b >> 1
        a = (a * a) % n
    return result

# returns 0 if prime, 'a' if composite with 'a' being the witness


def rabinMiller(n, u):
    a = random.randint(2, n-2)
    # a = 2
    print("a: " + str(a))

    b = modExponent(a, u, n)
    print("b: " + str(b))

    # prime
    if (b == 1 or b == n - 1):
        return 0

    print("--------")
    while (u < n-1):
        b = (b * b) % n
        u *= 2

        print("b: " + str(b))
        print("u: " + str(u))
        print("-------")
        # composite
        if (b == 1):
            return a

        # prime
        elif (b == n - 1):
            return 0

    # composite
    return a


n = 636127
print("n: " + str(n))
u = n - 1
print("u: " + str(u))
yeeee = False

while (u % 2 == 0):
    u = int(u/2)
print("u: " + str(u))

for i in range(25):
    witness = rabinMiller(n, u)
    if (witness != 0):
        print("composite with witness: " + str(witness))
        yeeee = True
        break
if (yeeee == False):
    print("prime!")
