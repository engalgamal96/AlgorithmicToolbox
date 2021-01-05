def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    f = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1, 1):
            f.append((f[i - 1] + f[i - 2]) % 10)
        x = f[n]
        return x


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
