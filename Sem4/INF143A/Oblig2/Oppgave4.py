
def setup():
    prime = int("""172471720944269739125606601541029487739340755626635
7725839713037594384191757726636695937218465501974427444
6965608060294664492706195111168863727536280366014000584
1509436858417187894094969161813013831722315776185924842
0990938995935683346965929645166170330762460615936845115
50344711963113062475271615663164060997""".replace("\n", ""))

    generator = 3
    dec = 333
    germanS = pow(generator, dec, prime)
    return prime, generator, germanS, dec


def signature():
    K = ephemeralKeyFinder(p)
    local_r = pow(g, K, p)
    message = int('A3FB8FCE', 16) % p
    local_s = ((message - (d * local_r)) * pow(K, -1, p - 1)) % (p - 1)
    return message, local_r, local_s


def verify():
    t = (pow(beta, r, p) * pow(r, s, p)) % p
    test = pow(g, m, p)
    if t == test:
        print("\nSignature verified")
    else:
        print("\nSignature is not verified")


def ephemeralKeyFinder(U):
    for i in range(U//2, U-1):
        result = computeGCD(i, U-1)
        if result == 1:
            return i
    return -1


def computeGCD(X, Y):
    while Y:
        X, Y = Y, X % Y

    return X


if __name__ == '__main__':
    p, g, beta, d = setup()

    print("\nThe public key is (prime, generator, beta): ")
    print("Prime:", p)
    print("Generator:", g)
    print("beta:", beta)

    m, r, s = signature()

    print("\nThe message can be represented as an integer mod p. This message is:", m)
    print("The signature (Message, (r, s):")
    print("r:", r)
    print("s:", s)

    verify()