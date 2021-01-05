def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    z = a
    y = b
    while b != 0:
        x = b
        b = a % b
        a = x
        if b == 0:
            gcd1 = a
    lcm = int((z * y) / gcd1)
    return lcm
if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
