def gcd_and_lcm(a, b):
    c = 2
    gcd = 1

    while (c <= a) and (c <= b):
        if (a % c == 0) and (b % c == 0):
            gcd *= c
            a //= c
            b //= c
        else :
            c += 1
    print(gcd)

    lcm = gcd * a * b
    print(lcm)


a, b = map(int, input().split())
gcd_and_lcm(a, b)