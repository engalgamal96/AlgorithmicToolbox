def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    result = int(n / 60) * 280
    n = n % 60
    f = [0, 1]
    if n <= 1:
        return n
    else:
        for i in range(2, n + 1, 1):
            f.append((f[i - 1] + f[i - 2]) % 10)
            result = result + (f[i - 1] + f[i - 2]) % 10
    return result
if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
