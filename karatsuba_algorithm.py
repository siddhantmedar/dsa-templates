def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = int(max(len(str(x)), len(str(y))))
    half = n // 2

    a = x // (10 ** half)
    b = x % (10 ** half)
    c = y // (10 ** half)
    d = y % (10 ** half)

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a + b, c + d) - a * c - b * d

    return ac * pow(10, (2 * half)) + ad_plus_bc * pow(10, half) + bd


print(karatsuba(146123,352120))
print(146123*352120)