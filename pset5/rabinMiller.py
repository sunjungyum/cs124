# https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

import random


def modExponent(a, b, n):
    result = 1
    a = a % n
    while (b > 0):
        if (b % 2 == 1):
            result = (result * a) % n
            b -= 1
        b /= 2
        a = (a * a) % n
    return result

# returns 0 if prime, 'a' if composite with 'a' being the witness


def rabinMiller(n, u):
    a = random.randint(2, n-2)
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


n = 294409
print(n)
u = n - 1
while (u % 2 == 0):
    u /= 2
print("u: " + str(u))

for i in range(25):
    witness = rabinMiller(n, u)
    if (witness != 0):
        print("composite with witness: " + str(witness))
        break

print("prime!")
