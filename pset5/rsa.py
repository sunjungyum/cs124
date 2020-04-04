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


# Identify public key
public_key = (46947848749720430529628739081, 37267486263679235062064536973)
n = public_key[0]
e = public_key[1]
print("n: " + str(n))
print("e: " + str(e) + "\n")

# Convert to binary
m = input("Enter plaintext: ")
m_bin = ''.join(format(ord(i), '08b') for i in m)
print("binary version: " + str(m_bin) + "\n")
m_dec = int(''.join(format(ord(i), '08b') for i in m), 2)
print("decimal version: " + str(m_dec) + "\n")

# Encrypt
c = modExponent(m_dec, e, n)
print("c: " + str(c) + "\n")
