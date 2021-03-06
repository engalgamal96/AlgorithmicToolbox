def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    from_index = from_index % 60
    f = [0, 1]
    if from_index > 1:
        for i in range(2, from_index + 2, 1):
            f.append((f[i - 1] + f[i - 2]))
    else:
        return from_index
    l = [f[from_index], f[from_index + 1]]
    result = f[from_index]
    v = to_index - from_index
    if v == 0:
        return f[from_index]
    elif v == 1:
        result = result + f[from_index + 1]
        return result
    else:
        result = result + f[from_index + 1]
        for i in range(2, v + 1, 1):
            l.append((l[i - 1] + l[i - 2]) % 10)
            result = result + (l[i - 1] + l[i - 2]) % 10
        return result % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
